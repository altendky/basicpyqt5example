import os
import pathlib


def collect(prefix, search_in, *extensions):
    for dir_name, subdirs, files in os.walk(search_in):
        for filename in (f for f in files if f.endswith(extensions)):
            filename = pathlib.Path(dir_name, filename)
            yield (filename, pathlib.Path(dir_name).relative_to(prefix))

#https://github.com/pyinstaller/pyinstaller/wiki/Recipe-Setuptools-Entry-Point
def Entrypoint(dist, group, name, **kwargs):
    import pkg_resources

    # get toplevel packages of distribution from metadata
    def get_toplevel(dist):
        distribution = pkg_resources.get_distribution(dist)
        if distribution.has_metadata('top_level.txt'):
            return list(distribution.get_metadata('top_level.txt').split())
        else:
            return []

    kwargs.setdefault('hiddenimports', [])
    packages = []
    for distribution in kwargs['hiddenimports']:
        packages += get_toplevel(distribution)

    kwargs.setdefault('pathex', [])
    # get the entry point
    ep = pkg_resources.get_entry_info(dist, group, name)
    # insert path of the egg at the verify front of the search path
    kwargs['pathex'] = [ep.dist.location] + kwargs['pathex']
    # script name must not be a valid module name to avoid name clashes on import
    script_path = os.path.join(workpath, name + '-script.py')
    print("creating script for entry point", dist, group, name)
    with open(script_path, 'w') as fh:
        print("import", ep.module_name, file=fh)
        print("%s.%s()" % (ep.module_name, '.'.join(ep.attrs)), file=fh)
        for package in packages:
            print("import", package, file=fh)

    return Analysis(
        [script_path] + kwargs.get('scripts', []),
        **kwargs,
    )

data_files = []

name = 'basicpyqt5example'

prefix = pathlib.Path('src')
search_in = prefix
extensions = ['.ui']
data_files.extend(collect(prefix, search_in, *extensions))

a = Entrypoint(
    dist=name,
    group='gui_scripts',
    name=name,
    pathex=['..'],
    datas=[(str(pathlib.Path(p).resolve()), pp) for p, pp in data_files],
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=None,
)

exe = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name=name,
    debug=False,
    strip=False,
    upx=True,
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name=name,
)