from setuptools import setup
import versioneer

setup(name='PDPbox',
      packages=['pdpbox'],
      package_data={'pdpbox': ['datasets/*/*']},
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='python partial dependence plot toolbox',
      author='SauceCat',
      author_email='jiangchun.lee@gmail.com',
      url='https://github.com/SauceCat/PDPbox',
      license='MIT',
      classifiers = [],
      install_requires=[
          'xgboost==1.3.3',
          'pandas~=1.3.5',
          'numpy~=1.22.1',
          'scipy~=1.5.2',
          'joblib~=1.1.0',
          'psutil~=5.9.0',
          'matplotlib~=3.4.2',
      ],
      zip_safe=False)
