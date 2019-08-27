import argparse
import init

parser = argparse.ArgumentParser()

parser.add_argument('name', nargs='+')
args = parser.parse_args()


for i in args.name:
    if i == 'init':
        init.initialize_project()