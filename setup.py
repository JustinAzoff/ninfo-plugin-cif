from setuptools import setup, find_packages

setup(name='ninfo-plugin-cifv2',
    version='0.3',
    zip_safe=False,
    packages = find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "ninfo>=0.1.11",
        "cifsdk",
    ],
    dependency_links=[
        "https://github.com/csirtgadgets/cif-sdk-py/archive/master.zip#egg=cifsdk",
    ],
    entry_points = {
        'ninfo.plugin': [
            'cifv2      = ninfo_plugin_cifv2',
        ]
    }
) 
