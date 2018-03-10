# Sample IoT MQTT Client

## Create empty python venv
```
python3.6 -m venv .venv
```

## Activate venv
```
source .venv/bin/activate
```

# Install required dependencies
```
pip install -r requirements.txt
```

# Install required dev dependencies if you want to edit the code
```
pip install -r requirements-dev.txt
```

# Run the sample device

Lookup your iot-gateway URL and configure a IoT-Device in AWS
```
python device.py a3p2mzola7m6q0.iot.eu-west-1.amazonaws.com 69142a4768
```