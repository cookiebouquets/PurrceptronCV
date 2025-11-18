import sensor, time, ml
from machine import LED
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.set_windowing((64, 64))
sensor.skip_frames(time=2000)

model = ml.Model("catbowl.tflite")
led = LED("LED_BLUE")
clock = time.clock()

while True:
    clock.tick()
    img = sensor.snapshot()
    pred = model.predict([img])[0][0]
    print("Pred:", pred[0], "FPS:", clock.fps())

    if pred[0] > 0.5:
        led.on()
    if pred[0] < 0.5:
        led.off()

    time.sleep(1)
