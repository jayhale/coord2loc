import os
import zlib
from pathlib import Path

import geopandas
import msgpack
import shapely
from pandas import DataFrame

BASE_DIR = Path(__file__).parent.parent
ADMIN_SHAPEFILE = BASE_DIR / "boundaries" / "geoBoundariesCGAZ_ADM1.shp"
OUTFILES_BASE = BASE_DIR / "packages"
ZLIB_COMPRESSION_LEVEL = 9

SELECTED_COUNTRIES = ["USA", "CAN"]


def save_data_for_country(
    country: str,
    polygons_df: DataFrame,
    compression_level: int = ZLIB_COMPRESSION_LEVEL,
):
    country = country.lower()

    print(f"({country}) saving {len(polygons_df)} polygons")

    wkb_bytes = msgpack.packb(
        [shapely.to_wkb(g, output_dimension=2) for g in polygons_df["geometry"]]
    )
    meta_bytes = msgpack.packb(
        polygons_df[["administrative_region", "country"]].to_dict("records")
    )

    wkb_outfile = (
        OUTFILES_BASE
        / f"coord2loc-{country}"
        / "src"
        / f"coord2loc_{country}"
        / "data"
        / "polygons.msgpack"
    )
    meta_outfile = (
        OUTFILES_BASE
        / f"coord2loc-{country}"
        / "src"
        / f"coord2loc_{country}"
        / "data"
        / "meta.msgpack"
    )

    if wkb_outfile.exists():
        os.remove(wkb_outfile)
    if meta_outfile.exists():
        os.remove(meta_outfile)

    wkb_outfile.write_bytes(zlib.compress(wkb_bytes, level=compression_level))
    print(f"({country}) wrote {wkb_outfile.relative_to(BASE_DIR)}")
    meta_outfile.write_bytes(zlib.compress(meta_bytes, level=compression_level))
    print(f"({country}) wrote {meta_outfile.relative_to(BASE_DIR)}")


def main() -> None:
    polygons_df = geopandas.read_file(ADMIN_SHAPEFILE)
    polygons_df = polygons_df[["shapeName", "shapeGroup", "geometry"]]
    polygons_df = polygons_df.rename(
        columns={"shapeName": "administrative_region", "shapeGroup": "country"}
    )

    print(f"Loaded {len(polygons_df)} polygons")

    for country in SELECTED_COUNTRIES:
        filtered_df = polygons_df[polygons_df["country"] == country]
        save_data_for_country(country, filtered_df)


if __name__ == "__main__":
    main()
