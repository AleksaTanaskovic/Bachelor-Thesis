from pylab import *
import vxi11

osc = vxi11.Instrument('147.91.8.139')
print(osc.ask('*idn?'))
osc.write('stop')
osc.write('wav:sour chan1')
osc.write('wav:mode norm')
osc.write('wav:form ascii')
osc.write('wav:star 1')
osc.write('wav:stop 120000')
data = osc.ask('wav:data?')
data2 = data[11:]
data3 = data2.split(',')
y = []
for i in range(0, len(data3)):
	y.append(float(data3[i]))
x = arange(0, len(data3))
osc.write('wav:sour chan2')
data_ = osc.ask('wav:data?')
data_2 = data_[11:]
data_3 = data_2.split(',')
yy = []
for i in range(0, len(data_3)):
	yy.append(float(data_3[i]))
xx = arange(0, len(data_3))
fig, ax = subplots()
ax.plot(x, y, label = 'Input signal', color = 'blue')
ax.plot(xx, yy, label = 'Output signal', color = 'red')
legend = ax.legend(loc = 'upper right', fontsize = 'x-large')
ylabel('U [V]')
xlabel('t [ms]')
show()
osc.close()