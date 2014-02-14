from setuptools import setup, find_packages

setup(name='ninfo-plugin-cif',
    version='0.3',
    zip_safe=False,
    packages = find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "ninfo>=0.1.11",
        "cif-http-client",
    ],
    entry_points = {
        'ninfo.plugin': [
            'cif      = ninfo_plugin_cif',
        ]
    }
) 
