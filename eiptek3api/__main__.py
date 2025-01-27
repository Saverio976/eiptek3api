import sys
import json
import argparse
import getpass

try:
    from eiptek3api.api import (
        Project,
        api_projects_all,
        EIP_TEK3_URL,
        CURRENT_SCHOLAR_YEAR,
    )
    from eiptek3api.filter import filter_it
    from eiptek3api.stats import full_stats
except ModuleNotFoundError:
    from api import Project, api_projects_all, EIP_TEK3_URL, CURRENT_SCHOLAR_YEAR
    from filter import filter_it
    from stats import full_stats


DUMP_PROJECTS_FILE = "dump_projects.json"


def filter_projects(projects: list[Project], filters: list[str]):
    _filters = []
    for _filter in filters:
        split_name, split_value = _filter.split("=", maxsplit=1)
        splited_name = split_name.split("__")
        _filters.append((splited_name, split_value))
    return filter_it(projects, _filters)


def dump_projects(projects: list[Project]):
    print(f"Writing {DUMP_PROJECTS_FILE}", file=sys.stderr)
    with open(DUMP_PROJECTS_FILE, mode="w") as f:
        json.dump([x.dict() for x in projects], f, indent=4)


def get_bearer():
    try:
        with open(".bearer", "r") as f:
            bearer = f.read().strip("\n ")
            return bearer
    except:
        bearer = getpass.getpass("Bearer: ")
        return bearer.strip("\n ")


class CMDLINEArg:
    year: int
    include_rejected: bool
    filters: list[str]
    dump_projects: bool

    def __init__(
        self, year: int, include_rejected: bool, filters: list[str], dump_projects
    ):
        self.year = year
        self.include_rejected = include_rejected
        self.filters = filters
        self.dump_projects = dump_projects


def get_cmdline_args():
    parser = argparse.ArgumentParser(
        description="CLI for https://eip-tek3.epitest.eu stats.",
        epilog="Made with 💜 by Saverio976",
    )
    parser.add_argument(
        "--year",
        type=int,
        nargs=1,
        help="2023 for Promo 2026 | 2024 for Promo 2027 | i.e.: the date of the third year for your promo",
    )
    parser.add_argument(
        "--include-rejected",
        action="store_const",
        const=True,
        default=False,
        help="Include project with status 'rejected'",
    )
    parser.add_argument(
        "--dump-projects",
        action="store_const",
        const=True,
        default=False,
        help=f"Write all projects details to a {DUMP_PROJECTS_FILE} file",
    )
    parser.add_argument(
        "filters",
        type=str,
        nargs="*",
        help="`field__eq=value` or `path__to__field__eq=value` or `field__contains=value`",
    )
    args = parser.parse_args()
    year = CURRENT_SCHOLAR_YEAR
    if args.year is not None and len(args.year) == 1:
        year = args.year[0]
    include_rejected = args.include_rejected
    filters = args.filters
    dump_projects = args.dump_projects
    args_class = CMDLINEArg(
        year=year,
        include_rejected=include_rejected,
        filters=filters,
        dump_projects=dump_projects,
    )
    print(f"Year: {args_class.year}", file=sys.stderr)
    print(f"Include Rejected: {args_class.include_rejected}", file=sys.stderr)
    print(f"Dump Projects: {args_class.dump_projects}", file=sys.stderr)
    print(f"Filters: {args_class.filters}", file=sys.stderr)
    return args_class


def main():
    args = get_cmdline_args()

    bearer = get_bearer()
    print("Loading data...", file=sys.stderr)
    projects = api_projects_all(
        bearer=bearer,
        scholar_year=args.year,
        include_rejected=args.include_rejected,
    )
    print("Loaded data.", file=sys.stderr)

    if len(args.filters) == 0:
        if args.dump_projects:
            dump_projects(projects.results)
        print(
            json.dumps(
                full_stats(projects.results),
                indent=4,
            )
        )
        return 0

    projs = filter_projects(projects.results, args.filters)
    if args.dump_projects:
        dump_projects(projs)
    stats = full_stats(projs)
    stats["proj_list"] = [EIP_TEK3_URL + "projects/" + str(proj.id) for proj in projs]
    print(
        json.dumps(
            stats,
            indent=4,
        )
    )


if __name__ == "__main__":
    sys.exit(main())
