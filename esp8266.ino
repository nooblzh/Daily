#include <ESP8266WiFi.h>
 
 
char ssid[] = "iPhone6s";        //  你家的路由器wifi名称
char paswd[] = "19980322";       // 你家的路由器wifi密码
void setup() {
  // put your setup code here, to run once:
   Serial.begin(115200);
   Serial.println();
 
   Serial.print("Connecting to ");
   Serial.println(ssid);
   WiFi.begin(ssid, paswd);                //开始连接wifi
 
   while (WiFi.status() != WL_CONNECTED)   //等待wifi连接成功
   {
      delay(500);
      Serial.print(".");
   }
   Serial.println("");
 
   Serial.println("WiFi connected");
   Serial.println("IP address: ");
   Serial.println(WiFi.localIP());     //打印连接上wifi后获取的ip地址
}
 
void loop() {
  // put your main code here, to run repeatedly:
 
}
