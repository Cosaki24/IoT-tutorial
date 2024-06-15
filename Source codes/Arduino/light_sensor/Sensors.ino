int light_sensor = ;  // pin number
int led = 13;  // built-in LED

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  while(!Serial)
    ;
  delay(1000);

  pinMode(light_sensor, INPUT);
  pinMode(led, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int light = analogRead(light_sensor);
  Serial.print("Light value: ");
  Serial.println(light);

  if(light < 300){
    digitalWrite(led, HIGH);
  } else {
    digitalWrite(led, LOW);
  }

  delay(1000);
}
