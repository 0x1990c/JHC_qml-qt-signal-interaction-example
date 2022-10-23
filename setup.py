from setuptools import setup, find_packages


setup(
    name='qml-qt-signal-interaction-example',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'qml-qt-signal-interaction-example': ['slider.qml']},
    description='QML, QT interaction example using signal',
    url='https://github.com/yjg30737/qml-qt-signal-interaction-example.git',
    long_description_content_type='text/markdown',
    install_requires=[
        'PyQt5>=5.12'
    ]
)