import os,sys
import setuptools

if __name__ == '__main__':
    try:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
            long_description = f.read()
    except Exception:
        long_description = ''

    setuptools.setup(
        name='iconfinder',
        version='0.1',
        author="digfish",
        author_email="digfish@digfish.org",
        description=(
            "Easily get the icon associated with an executable in every OS"
        ),
        long_description=long_description,
        long_description_content_type='text/markdown',
        license="Apache License 2.0",
        url="https://github.com/digfish/iconfinder",
        packages=setuptools.find_packages(),
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Environment :: Win32 (MS Windows)",
            "Environment :: MacOS X",
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: MacOS",
            "Operating System :: POSIX :: Linux"
        ],
        entry_points={
            'console_scripts': [
                'iconfinder=iconfinder.finder:main'
            ],
        },
        include_package_data=True,
        package_data={},
        install_requires=['pywin32','pyxdg','Pillow']
    )
