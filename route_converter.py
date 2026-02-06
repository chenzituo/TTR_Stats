#!/usr/bin/env python3
import argparse
import csv
import json
from pathlib import Path


TYPE_MAP = {
    "land": "train",
    "ocean": "ship",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert routes from board JSON to CSV."
    )
    parser.add_argument(
        "--input",
        "-i",
        default="board.json",
        help="Path to input JSON (default: board.json)",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="routes.csv",
        help="Path to output CSV (default: routes.csv)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)

    with input_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    places = {p["id"]: p["name"] for p in data.get("places", [])}
    roads = data.get("roads", [])

    with output_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["start", "end", "type", "color", "length"])

        for road in roads:
            place_ids = road.get("placeIds", [])
            if len(place_ids) != 2:
                continue

            start = places.get(place_ids[0], str(place_ids[0]))
            end = places.get(place_ids[1], str(place_ids[1]))

            route_type = road.get("routeType", "land")
            mapped_type = TYPE_MAP.get(route_type, route_type)

            length = road.get("spaceAmount")
            for lane in road.get("lanes", []):
                color = lane.get("colour", "")
                writer.writerow([start, end, mapped_type, color, length])

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
