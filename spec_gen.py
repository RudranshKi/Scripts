import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf
from matplotlib.backends.backend_pdf import PdfPages 

file_spec = "spec.csv"
file_corner = "corner_sim_inv.csv"
file_corner_ref = "corner_detes.csv"

spec_data =  []
spec_data = np.loadtxt(file_spec , delimiter="," , unpack=True , dtype=str)
spec_data = list(np.transpose(spec_data))
spec_headers = ['Spec Name', 'Specs Description', 'Min', 'Typ', 'Max','Min corner','Max Corner','unit']
table_spec = tabulate(spec_data,headers=spec_headers,tablefmt = "pretty")

print(table_spec)

corner_data = []
corner_cp = []
corner_data = np.loadtxt(file_corner , delimiter="," , unpack=True , dtype=str)
corner_cp = corner_data
corner_data = corner_data[0:len(corner_data)-1]
corner_data = list(np.transpose(corner_data))
corner_headers = ['Corner name','TRise (in nS)','TFall (in nS)']
table_corner = tabulate(corner_data,headers=corner_headers,tablefmt="pretty")

print(table_corner)

corner_ref_data= []
corner_ref_data = np.loadtxt(file_corner_ref , delimiter="," , unpack=True , dtype=str)
corner_ref_data = corner_ref_data[0:len(corner_ref_data)-1]
corner_ref_data = list(np.transpose(corner_ref_data))
corner_ref_headers = ['Corner name','temperature','VSup']
table_corner_ref = tabulate(corner_ref_data,headers=corner_ref_headers,tablefmt="pretty")

print(table_corner_ref)

rise_times = [float(item[1]) for item in corner_data]
fall_times = [float(item[2]) for item in corner_data]
# Generate x-axis labels (specs names)
specs_names = [item[0] for item in corner_data]


fig, axs = plt.subplots(2, 1, figsize=(25, 15))

# Plot data on the first subplot
axs[0].plot(specs_names, rise_times, marker='o', linestyle='-')
axs[0].set_title('RISE TIME',fontsize=25)
axs[0].set_xlabel('Corner  ------->',fontsize=20)
axs[0].set_ylabel('Rise Time (in nS) -------->',fontsize=20)
for tick in axs[0].get_xticklabels() + axs[0].get_yticklabels():
    tick.set_fontsize(20)

# Plot data on the second subplot
axs[1].plot(specs_names, fall_times, marker='o', linestyle='-')
axs[1].set_title('FALL TIME',fontsize=25)
axs[1].set_xlabel('Corner  ------->',fontsize=20)
axs[1].set_ylabel('Fall Time (in nS) -------->',fontsize=20)
for tick in axs[1].get_xticklabels() + axs[1].get_yticklabels():
    tick.set_fontsize(20)
plt.tight_layout()

pdf_filename = "Spec_sheet.pdf"
pdf = matplotlib.backends.backend_pdf.PdfPages(pdf_filename)
fig_table = plt.figure(figsize=(25, 15))

plt.text(0.5, 0.99, "Table 1: Specification Data", {'fontname': 'Courier New', 'fontsize': 24, 'fontweight': 'bold'}, ha='center')
plt.text(0.01, 0.84, table_spec, {'fontname': 'Courier New', 'fontsize': 22 , 'fontweight': 'bold'})
plt.text(0.2, 0.80, "Table 2: Corner Data", {'fontname': 'Courier New', 'fontsize': 24, 'fontweight': 'bold'}, ha='center')
plt.text(0.01, 0.42, table_corner, {'fontname': 'Courier New', 'fontsize': 22 , 'fontweight': 'bold'})
plt.text(0.2, 0.38, "Table 3: Corner Reference", {'fontname': 'Courier New', 'fontsize': 24, 'fontweight': 'bold'}, ha='center')
plt.text(0.01, 0.0001, table_corner_ref, {'fontname': 'Courier New', 'fontsize': 22 , 'fontweight': 'bold'})
plt.axis('off')
pdf.savefig(fig_table)
plt.close(fig_table)

pdf.savefig(fig)
plt.close(fig)

pdf.close()