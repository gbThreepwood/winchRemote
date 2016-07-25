# winchRemote
GNU Radio software for communication with a remote controlled winch.

The controller has the following label:
```
Model:KLS-203
12V/433MHZ
ON, 00013425
```

The remote control has two buttons "OUT" and "IN" for commanding the rotational direction of the winch. It appears to be utilizing on-off keying, transmitting at a frequency of about 433.9MHz.

By capturing the transmitted data from the remote, and interpretating a short signal as binary zero, and a long signal as binary one, the following patterns emerged:

- OUT-command: 00111100 11010101 000000110
- IN-command:  00111100 11010101 000011000


The pattern is repeatedly transmitted as long as the button is pressed. The transmission lasts for about 50ms, with a pause of about 15ms between each transmission.

The symbol length is about 0.75 ms. The tx pattern is off-on-x, where x is off for binary zero, and on for binary one.

## Signal capture
A simple GNU Radio block diagram is used to capture the signals. The complex to mag block demodulates the on-off keyed signal.

![alt tag](https://raw.githubusercontent.com/gbThreepwood/winchRemote/master/signal-capture.grc.png)
