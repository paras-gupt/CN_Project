import pandas as pd
import matplotlib.pyplot as plt

a = r"C:\Users\Paras_Gupta\Desktop\CNProject\tsv_results_RTT\nginx_rr_ab.tsv"
# a = "1_server_load_balanced.tsv"
b = r"C:\Users\Paras_Gupta\Desktop\CNProject\tsv_results_RTT\nginx_leastconn_ab.tsv"

c = r"C:\Users\Paras_Gupta\Desktop\CNProject\tsv_results_RTT\nginx_iphash_ab.tsv"

df=  pd.read_csv(str(a), sep = '\t')
df_=  pd.read_csv(str(b), sep = '\t')
df_3 = pd.read_csv(str(c), sep = '\t')

column = list(df.columns.values)[4]
df1= df[column]
df2 = df_[column]
df3 = df_3[column]
plt.plot(df1[:-1], label = "Round Robin LB Nginx")
# plt.plot(df1[:-1], label = "w/o Load Balancing")
# plt.hold()
plt.plot(df2[:-1], label = "Least Connections LB Nginx")
# plt.plot(df2[:-1], label = " w/ Load Balancing")
plt.plot(df3[:-1], label = "IP Hash LB Nginx")
plt.legend()
plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt

# a = r"C:\Users\Paras_Gupta\Desktop\CNProject\tsv_results_RTT\haproxy_l7_leastconn_ab.tsv"
# # a = "1_server_load_balanced.tsv"
# b = r"C:\Users\Paras_Gupta\Desktop\CNProject\tsv_results_RTT\nginx_leastconn_ab.tsv"

# df=  pd.read_csv(str(a), sep = '\t')
# df_=  pd.read_csv(str(b), sep = '\t')

# column = list(df.columns.values)[4]
# df1= df[column]
# df2 = df_[column]
# plt.plot(df1[:-1], label = "Least Connections LB HAProxy")
# # plt.plot(df1[:-1], label = "w/o Load Balancing")
# # plt.hold()
# plt.plot(df2[:-1], label = "Least Connections LB Nginx")
# # plt.plot(df2[:-1], label = " w/ Load Balancing")
# plt.legend()
# plt.show()