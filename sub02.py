{\rtf1\ansi\ansicpg932\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fmodern\fcharset0 CourierNewPSMT;\f1\fmodern\fcharset0 CourierNewPS-BoldMT;}
{\colortbl;\red255\green255\blue255;\red15\green114\blue1;\red255\green255\blue255;\red32\green32\blue32;
\red10\green82\blue135;\red0\green0\blue0;\red251\green0\blue129;\red0\green0\blue255;\red18\green139\blue2;
}
{\*\expandedcolortbl;;\cssrgb\c0\c50980\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c16863\c16863\c16863;
\cssrgb\c0\c40000\c60000;\cssrgb\c0\c0\c0;\cssrgb\c100000\c7843\c57647;\cssrgb\c0\c0\c100000;\cssrgb\c0\c60000\c0;
}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl308\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # -*- coding: utf-8 -*- \cf4 \strokec4 \
\pard\pardeftab720\sl308\partightenfactor0

\f1\b \cf5 \strokec5 import
\f0\b0 \cf4 \strokec4  \cf6 \strokec6 paho.mqtt.client as mqtt\cf4 \strokec4 \
\'a0\

\f1\b \cf5 \strokec5 def
\f0\b0 \cf4 \strokec4  \cf6 \strokec6 on_connect(client, userdata, rc):\cf4 \strokec4 \
\'a0\'a0\cf7 \strokec7 print\cf6 \strokec6 (\cf8 \strokec8 "Connected with result code "\cf4 \strokec4  
\f1\b \cf5 \strokec5 +
\f0\b0 \cf4 \strokec4  \cf7 \strokec7 str\cf6 \strokec6 (rc))\cf4 \strokec4 \
\'a0\'a0\cf6 \strokec6 client.subscribe(\cf8 \strokec8 "hello/world"\cf6 \strokec6 )\cf4 \strokec4 \
\'a0\

\f1\b \cf5 \strokec5 def
\f0\b0 \cf4 \strokec4  \cf6 \strokec6 on_disconnect(client, userdata, rc):\cf4 \strokec4 \
\'a0\'a0
\f1\b \cf5 \strokec5 if
\f0\b0 \cf4 \strokec4 \'a0 \cf6 \strokec6 rc !
\f1\b \cf5 \strokec5 =
\f0\b0 \cf4 \strokec4  \cf9 \strokec9 0\cf6 \strokec6 :\cf4 \strokec4 \
\'a0\'a0\'a0\'a0\cf7 \strokec7 print\cf6 \strokec6 (\cf8 \strokec8 "Unexpected disconnection."\cf6 \strokec6 )\cf4 \strokec4 \
\'a0\

\f1\b \cf5 \strokec5 def
\f0\b0 \cf4 \strokec4  \cf6 \strokec6 on_message(client, userdata, msg):\cf4 \strokec4 \
\'a0\'a0\cf7 \strokec7 print\cf6 \strokec6 (\cf8 \strokec8 "Received message '"\cf4 \strokec4  
\f1\b \cf5 \strokec5 +
\f0\b0 \cf4 \strokec4  \cf7 \strokec7 str\cf6 \strokec6 (msg.payload) 
\f1\b \cf5 \strokec5 +
\f0\b0 \cf4 \strokec4  \cf8 \strokec8 "' on topic '"\cf4 \strokec4  
\f1\b \cf5 \strokec5 +
\f0\b0 \cf4 \strokec4  \cf6 \strokec6 msg.topic 
\f1\b \cf5 \strokec5 +
\f0\b0 \cf4 \strokec4  \cf8 \strokec8 "' with QoS "\cf4 \strokec4  
\f1\b \cf5 \strokec5 +
\f0\b0 \cf4 \strokec4  \cf7 \strokec7 str\cf6 \strokec6 (msg.qos))\cf4 \strokec4 \
\'a0\
\pard\pardeftab720\sl308\partightenfactor0
\cf6 \strokec6 client 
\f1\b \cf5 \strokec5 =
\f0\b0 \cf4 \strokec4  \cf6 \strokec6 mqtt.Client()\cf4 \strokec4 \
\cf6 \strokec6 client.on_connect 
\f1\b \cf5 \strokec5 =
\f0\b0 \cf4 \strokec4  \cf6 \strokec6 on_connect\cf4 \strokec4 \
\cf6 \strokec6 client.on_disconnect 
\f1\b \cf5 \strokec5 =
\f0\b0 \cf4 \strokec4  \cf6 \strokec6 on_disconnect\cf4 \strokec4 \
\cf6 \strokec6 client.on_message 
\f1\b \cf5 \strokec5 =
\f0\b0 \cf4 \strokec4  \cf6 \strokec6 on_message\cf4 \strokec4 \
\'a0\
\cf6 \strokec6 client.connect(\cf8 \strokec8 "localhost"\cf6 \strokec6 , \cf9 \strokec9 1883\cf6 \strokec6 , \cf9 \strokec9 60\cf6 \strokec6 ) \cf4 \strokec4 \
\'a0\
\cf6 \strokec6 client.loop_forever()\cf4 \strokec4 \
}