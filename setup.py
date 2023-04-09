from setuptools import setup

setup(name = 'myLib',
      version = '1.0',
      description = 'Package containing Linear, nodes and trees',
      author = 'Marcus Kittelson & Rodmichael Umapas',
      packages = ['myLib', 'myLib.datastructures', 'myLib.datastructures.Linear', 'myLib.datastructures.nodes', 'myLib.datastructures.trees']
)