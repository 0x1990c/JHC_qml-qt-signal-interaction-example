# qml-qt-signal-interaction-example
QML, QT interaction with signal example (using PyQt)

## Detailed Description
Simple PyQt GUI except for QML type Slider.

Slider sends the "moved" event when handle being moved as you can see the `slider.qml`'s code.

PyQt script(`main.py`) gets that event and handles it properly. In this case, it changes the QLabel's text.

## Requirements
* PyQt5 >= 5.12 - for using `onMoved` event of QML Slider (supported since QtQuick.Controls 2.2/Qt 5.9)

See <a href="https://doc.qt.io/qt-6/qtquickcontrols-index.html#versions">more information here</a> about the version of Qt, QtQuick, etc.

## Install
`git clone https://github.com/yjg30737/qml-qt-signal-interaction-example.git`

## Preview

https://user-images.githubusercontent.com/55078043/197387063-20e8706b-2ab3-412a-ad74-9164991cca34.mp4
