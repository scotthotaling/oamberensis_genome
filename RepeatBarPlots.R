
#################### This one makes bar plots in Fig. 2a  #####################
library (ggplot2)

in_data5<-read.table("Fig2a_repeatmasker_plot_data.txt", header = TRUE)
print(in_data5)

bar_cols<-c("#D3D3D3", "#E5A229", "#9DC8EB", "#F2AAF2", "#9D4C9C", "#CE7A7A", "#79A461", "#4260AC")
#in_data5$Taxon <- factor(in_data5$Taxon, levels = in_data5$Taxon)

in_data5$Taxon <- factor(in_data5$Taxon, levels =unique(in_data5$Taxon))

ggplot(data = in_data5, aes(x = Taxon, y = TotalBases, fill = Repeat)) +
  geom_bar(stat='identity') + theme_bw() + scale_fill_manual(values=bar_cols)
  #theme(legend.position = "top")

#################### This one summarizes TE categories -- Fig2b #####################
library (ggplot2)

in_data5<-read.table("Fig2b_group_summaries3.txt", header = TRUE)
print(in_data5)

bar_cols<-c("#D3D3D3", "#E5A229", "#9DC8EB", "#F2AAF2", "#BEE0BD", "#8A181B", "#CE7A7A", "#9D4C9C", "#79A461", "#4260AC")
#in_data5$Taxon <- factor(in_data5$Taxon, levels = in_data5$Taxon)

in_data5$Taxon <- factor(in_data5$Taxon, levels =unique(in_data5$Taxon))

ggplot(data = in_data5, aes(group_repeat, TotalBases, fill = major_group)) +
  geom_boxplot() + theme_bw() + theme(axis.text.x=element_text(angle=90,hjust=1)) #+ coord_flip() #+ geom_jitter(width = 0.2)  #+ scale_fill_manual(values=bar_cols)

ggplot(data = in_data5, aes(group_repeat, AssemblyPercent, fill = major_group)) +
  geom_boxplot() + theme_bw() + theme(axis.text.x=element_text(angle=90,hjust=1)) #+ coord_flip() #+ geom_jitter(width = 0.2) + theme_bw() #+ scale_fill_manual(values=bar_cols)

