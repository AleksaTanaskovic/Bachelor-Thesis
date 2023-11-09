from pylab import *
import vxi11
import time

fg = vxi11.Instrument('147.91.9.108')
osc = vxi11.Instrument('147.91.8.139')
print(fg.ask('*idn?'))
print(osc.ask('*idn?'))
f = 20
df = 1
fg.write('sour1:appl:sin 20,2')
osc.write('aut')
ch1 = [0] * 70
ch2 = [0] * 70
for i in range(0, 70):
	fk = f + i * df
	fg.write('sour1:appl:sin '+str(fk)+',2')
	time.sleep(0.3)
	ch1[i] = float(osc.ask('meas:vmax? chan1'))
	ch2[i] = float(osc.ask('meas:vmax? chan2'))
n = [0] * 70
for i in range(0, len(ch1)):
	n[i] = 20 * math.log(ch2[i] / ch1[i], 10)
z = arange(20, 90, df)
fr = open("frek", "r")
g = open("slabljenje", "r")
x_axis = fr.read()
y_axis = g.read()
x = x_axis.split('\n')
y = y_axis.split('\n')
a = x[:-1]
b = y[:-1]
xx = []
yy = []
for i in range(len(a)):
	xx.append(float(a[i]))
	yy.append(float(b[i]))
fig, ax = subplots()
ax.plot(z, n, label = 'Realized', color = 'blue')
ax.plot(xx, yy, 'x', label = 'FILTER42', color = 'red')
legend = ax.legend(loc = 'center right', fontsize = 'x-large')
ylabel('|H(jf)| [dB]')
xlabel('f [Hz]')
xlim(10, 100)
ylim(-30, 10)
show()
fg.close()
osc.close()