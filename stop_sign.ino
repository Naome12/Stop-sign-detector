const int motorPin = 13;

void setup()
{
    pinMode(motorPin, OUTPUT);
    Serial.begin(9600);
    Serial.println("Ready to receive UART commands...");
}

void loop()
{
    if (Serial.available())
    {
        char command = Serial.read();

        if (command == '1')
        {
            // Stop the robot (turn off motor / turn on LED)
            digitalWrite(motorPin, LOW);
            Serial.println("Received 1: STOP");
        }
        else if (command == '0')
        {
            // Keep moving (turn on motor / turn off LED)
            digitalWrite(motorPin, HIGH);
            Serial.println("Received 0: MOVE");
        }
    }
}
