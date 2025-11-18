import sensor, time, ml

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.set_windowing((64, 64))
sensor.skip_frames(time=2000)

model = ml.Model("catbowl.tflite")


clock = time.clock()

while True:
    clock.tick()
    img = sensor.snapshot()
    pred = model.predict([img])[0][0]
    print("Pred:", pred, "FPS:", clock.fps())
