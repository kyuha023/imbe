<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>397</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QWidget" name="verticalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>401</width>
     <height>301</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout">
    <item>
     <widget class="QLabel" name="label">
      <property name="text">
       <string>TextLabel</string>
      </property>
     </widget>
    </item>
    <item alignment="Qt::AlignBottom">
     <widget class="QPushButton" name="PushButton">
      <property name="text">
       <string>clear</string>
      </property>
     </widget>
    </item>
    <item>
     <widget class="QLineEdit" name="lineEdit"/>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections>
  <connection>
   <sender>PushButton</sender>
   <signal>clicked()</signal>
   <receiver>lineEdit</receiver>
   <slot>clear()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>219</x>
     <y>288</y>
    </hint>
    <hint type="destinationlabel">
     <x>229</x>
     <y>260</y>
    </hint>
   </hints>
  </connection>
  <connection>
   <sender>PushButton</sender>
   <signal>clicked()</signal>
   <receiver>label</receiver>
   <slot>clear()</slot>
   <hints>
    <hint type="sourcelabel">
     <x>273</x>
     <y>289</y>
    </hint>
    <hint type="destinationlabel">
     <x>283</x>
     <y>180</y>
    </hint>
   </hints>
  </connection>
  <connection>
   <sender>lineEdit</sender>
   <signal>textChanged(QString)</signal>
   <receiver>label</receiver>
   <slot>setText(QString)</slot>
   <hints>
    <hint type="sourcelabel">
     <x>149</x>
     <y>252</y>
    </hint>
    <hint type="destinationlabel">
     <x>150</x>
     <y>168</y>
    </hint>
   </hints>
  </connection>
 </connections>
</ui>
