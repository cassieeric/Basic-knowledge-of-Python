import matplotlib.pyplot as plt

# def autolabel(rects):
#     for rect in rects:
#         height = rect.get_height()
#         plt.text(rect.get_x()+rect.get_width()/2., 1.04*height, '%s'%float(height))
#
# plt.xlabel('sex')
# plt.ylabel('number')
# plt.xticks((0, 1), ('male', 'female'))
# plt.title('sex ratio analysis')
# x = [866, 665, 98]
# rect = plt.bar(left=(0, 1000), height=(866, 665), width=0.25, align='center', yerr=0.0001)
# plt.legend(rect, ['number'], bbox_to_anchor=(0.95, 0.95))
# autolabel(rect)
# plt.show()


# x = [866, 665, 98]
#
# labels = ['Unknown', 'Male', 'Female']
#
# fig = plt.figure()
# plt.title("WeChat's circle gender ratio")
#
#
# rect = plt.bar(x, 800, width=0.35, color='r', yerr=womenStd, align='center', labels=labels)
# plt.legend(rect, ['number'],  bbox_to_anchor=(0.95, 0.95))
# plt.show()
# plt.savefig("BarChart.jpg")

x = [1, 2, 3]
y = [866, 665, 98]

plt.figure(figsize=(15, 10), dpi=80)
labels = ['Unknown', 'Male', 'Female']
plt.title('sex ratio analysis')


plt.bar(x, y, width=0.5, align='center', facecolor='yellowgreen', edgecolor='white')

plt.xlabel('sex')
plt.ylabel('number')

for a, b in zip(labels, y):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va='bottom', fontsize=12)


plt.title('Sex distribution plot')

plt.show()

