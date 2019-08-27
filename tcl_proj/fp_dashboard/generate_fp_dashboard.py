#!/usr/bin/env python
'''*************************************************************************************************************
@summary  : Generates the Feasibility and Pricing Dashboard by fetching data from MYSQL DB.
@author   : Aparna Rao Kota
*************************************************************************************************************'''

import os
import sys
from datetime import datetime
sys.path.append("C:/Users/IT/PycharmProjects/my_project/")
from header_template import Template as TE
from sql_template import SqlTemplate as ST
import MySQLdb

# Connect to MySQL Database
db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="Starangel@9", db="oms")
cur = db.cursor()

class SamplePivotGenerator:
    def __init__(self):
        '''Initializing
        '''
        print("Initializing the generation of Feasibilty and Pricing Dashboard...")

        
    def get_row_content(self):
        '''Gets the row labels
        '''
        price_list, prod_list, fmp_list, mfmp_list, fp_list, mfp_list, prod_dict = self.get_site_level_content()
        pivot_dict = prod_dict
        row_content = " "
        for row_label in pivot_dict:
            fmp = pivot_dict[row_label]["FMP"]
            mfmp = pivot_dict[row_label]["MFMP"]
            fp = pivot_dict[row_label]["FP"]
            mfp = pivot_dict[row_label]["MFP"]
            
            
            row_content += '''<tr  bgcolor="{3}">
                              <td><strong>{0}</strong></td>
                              <td>{1}</td>
                              <td>{2}</td>
                              <td>{4}</td>
                              <td>{5}</td>
                              </tr>'''.format(row_label,
                                              fmp,
                                              mfmp,
                                              "FFFFFF",
                                              fp, mfp)
        row_content += "</div>"
        row_content += "</tbody>"
        row_content += "</table>"
        row_content += "</div>"

        return row_content

    
    def get_sub_row_content(self):
        '''Gets the sub row labels
        '''
        share_dict = {"10-20" : "10%",
              "20-30" : "20%",
              "30-40" : "30%",
              "40-50" : "40%"}
        sub_row_content = " "
        for mrc_dev in share_dict:
            share = share_dict[mrc_dev]

            sub_row_content += '''<tr  bgcolor="{2}">
                              <td><strong>{0}</strong></td>
                              <td>{1}</td>
                              </tr>'''.format(mrc_dev,
                                              share,
                                              "FFFFFF")
        sub_row_content += "</div>"
        sub_row_content += "</tbody>"
        sub_row_content += "</table>"
        sub_row_content += "</div>"
        return sub_row_content
    
    
    def get_order_level_content(self):
        '''Returns the price list for order level
        '''
        sel_1_cmd = ST.sel_1_cmd
        cur.execute(sel_1_cmd) #based on order level
        row_tup = cur.fetchall()
        order_prod_dict = {}
        order_prod_list = []
        order_fmp_list = []
        order_mfmp_list = []
        order_fp_list = []
        order_mfp_list = []

        for row in row_tup:
            prod_name = row[0]
            fmp = row[3]
            mfmp = row[7]
            fp = row[1]
            mfp = row[5]
    
            order_prod_dict[prod_name] = {"FMP" : fmp, "MFMP" : mfmp}
            order_prod_list.append(prod_name)
            order_fmp_list.append(int(fmp))
            order_mfmp_list.append(int(mfmp))
            order_fp_list.append(int(fp))
            order_mfp_list.append(int(mfp))
        return order_prod_list, order_fmp_list, order_mfmp_list, order_fp_list, order_mfp_list

    
    def get_site_level_content(self):
        '''Returns the price list for site level
        '''
        sel_2_cmd = ST.sel_2_cmd
        cur.execute(sel_2_cmd) #Based on site level
        row_tup = cur.fetchall()

        prod_dict = {}
        prod_list = []
        fmp_list = []
        mfmp_list = []
        fp_list = []
        mfp_list = []

        price_list = []
        price_dict = {}
        fp_dict = {}
        fmp_dict = {}
        mfmp_dict = {}
        mfp_dict = {}

        for row in row_tup:
            prod_name = row[0]
            fp = row[1]
            fmp = row[3]
            mfp = row[5]
            mfmp = row[7]
    
            prod_dict[prod_name] = {"FMP" : fmp, "MFMP" : mfmp, "FP": fp, "MFP" : mfp}
            prod_list.append(prod_name)
            fmp_list.append(int(fmp))
            mfmp_list.append(int(mfmp))
            fp_list.append(int(fp))
            mfp_list.append(int(mfp))
            price_list.append((int(mfmp), int(fmp), int(mfp), int(fp)))

        return price_list, prod_list, fmp_list, mfmp_list, fp_list, mfp_list, prod_dict
    
    
    def get_deviation_slab_level_content(self):
        '''Returns the deviation slab level content
        '''
        sel_3_cmd = ST.sel_3_cmd
        cur.execute(sel_3_cmd) #Based on dev slab level
        row_tup_3 = cur.fetchall()

        row_list = ['0-5%-Over', '100%-Over', '15-50%-Over', '15-50%-Under', '5-0%-Under',
                     '5-0%-Over', '5-15%-Under', '50-100%-Over', '50-100%-Under']

        dev_slab_list = []
        arc_dev_list = []
        nrc_dev_list = []
        acv_dev_list = []
        
        nrc_dev_slab_list = []
        nrc_slab_list = []
        #dev_slab_dict = {}
        arc_15_50_count = 0
        for row in row_tup_3:
            dev_type = row[0]
            slab_val = row[1]
            total_sites = int(row[10])
            dev_slab_list.append((dev_type, slab_val, total_sites))
            # dev_slab_list.append(('NRC', '5-0%-Over', 0))
            # dev_slab_list.sort()
        dev_slab_list.append(('NRC', 'b_5-15%-Over', 0))
        dev_slab_list.sort()

        for value in dev_slab_list:
            dev_type, slab_val, total_sites = value
            if dev_type == "ARC":
                arc_dev_list.append(total_sites)
            
            if dev_type == "NRC":
                # nrc_slab_list.append(slab_val)
                nrc_dev_list.append(total_sites)
                
            if dev_type == "ACV":
                acv_dev_list.append(total_sites)
        return arc_dev_list, nrc_dev_list, acv_dev_list
    
    def get_component_level_content(self):
        '''Returns the component level content
        '''
        sel_5_cmd = ST.sel_5_cmd
        cur.execute(sel_5_cmd) #Based on dev slab level
        row_tup_5 = cur.fetchall()
        
        arc_list = []
        nrc_list = []
        
        arc_list.append(row_tup_5[0][2])
        arc_list.append(row_tup_5[0][4])
        arc_list.append(row_tup_5[0][0])
        
        nrc_list.append(row_tup_5[0][3])
        nrc_list.append(row_tup_5[0][5])
        nrc_list.append(row_tup_5[0][1])
        
        return arc_list, nrc_list

    
    def get_npl_data(self):
        '''Returns the NPL data
        '''
        sel_6_cmd = ST.sel_6_cmd
        cur.execute(sel_6_cmd) #Based on chronological level
        row_tup = cur.fetchall()
        
        npl_list = []
        npl_fmp_list = []
        npl_fp_list = []
        npl_mfmp_list = []
        npl_mfp_list = []
        
        for row in row_tup:
            prod_name = row[0]
            status = row[1]
            year =str(row[4])
            month = str(row[5])[:3]
            count = int(row[6])
            
            if (prod_name == "NPL"):
                label_name = prod_name + "-" + status
                year_name = month + "-" + year
                npl_list.append((label_name, year_name, count))
                                    
                if (label_name == "NPL-FMP"):
                    npl_fmp_list.append((label_name, year_name, count))
                    npl_fmp_list_mod = self.modify_zero_month_year(npl_fmp_list)
                if (label_name == "NPL-FP"):
                    npl_fp_list.append((label_name, year_name, count))
                    npl_fp_list_mod = self.modify_zero_month_year(npl_fp_list)
                if (label_name == "NPL-MFMP"):
                    npl_mfmp_list.append((label_name, year_name, count))
                    npl_mfmp_list_mod = self.modify_zero_month_year(npl_mfmp_list)
                if (label_name == "NPL-MFP"):
                    npl_mfp_list.append((label_name, year_name, count))
                    npl_mfp_list_mod = self.modify_zero_month_year(npl_mfp_list)
        return npl_fmp_list_mod, npl_fp_list_mod, npl_mfmp_list_mod, npl_mfp_list_mod
        
        
    def modify_zero_month_year(self, ex_list):
        '''Returns 0 count for the month/year not present
        '''
        zero_list = []
        ex_year_list = []
        count_list = []
        
        my_list = ["Aug-2018", "Sep-2018", "Oct-2018", "Nov-2018", "Dec-2018", "Jan-2019", "Feb-2019", "Mar-2019", "Apr-2019", "May-2019", "Jun-2019"]

        for (prod, year, cnt) in ex_list:
            ex_year_list.append(year)
        for each_year in my_list:
            if not (each_year) in ex_year_list:
                cnt = 0
                zero_list.append((prod, each_year, cnt))
        new_list = ex_list + zero_list
        new_list.sort(key = lambda date: datetime.strptime(date[1], '%b-%Y')) 
        for each_item in new_list:
            cnt = each_item[2]
            count_list.append(cnt)
        return count_list
        
    def get_chronological_data(self):
        '''Returns the chronological content data
        '''
        sel_6_cmd = ST.sel_6_cmd
        cur.execute(sel_6_cmd) #Based on chronological level
        row_tup = cur.fetchall()
        
        chrono_list = []
        label_list = []
        year_list = []     
        
        ias_fmp_onnet_wireline_list= []
        ias_fmp_onnet_wireless_list = []
        ias_fmp_offnet_wireless_list = []
        
        ias_fp_onnet_wireline_list = []
        
        ias_mfmp_offnet_wireless_list = []
        ias_mfmp_onnet_wireless_list = []
        ias_mfmp_onnet_wireline_list = []
        
        gvpn_fp_onnet_wireless_list = []
        
        gvpn_fmp_onnet_wireline_list = []
        
        gvpn_mfmp_onnet_wireline_list = []
        
             
        for row in row_tup:
            prod_name = row[0]
            status = row[1]
            cable_type = row[2].lower()
            net_type = row[3].lower()
            year =str(row[4])
            month = str(row[5])[:3]
            count = int(row[6])
            
            if not (prod_name == "NPL"):
                label_name = prod_name + "-" + status + "-" + net_type + "-" + cable_type
                year_name = month + "-" + year
                label_list.append(label_name)
                year_list.append(year_name)
                chrono_list.append((label_name, year_name, count))
                                    
                
                if (label_name == "IAS-FMP-onnet-wireline"):
                    ias_fmp_onnet_wireline_list.append((label_name, year_name, count))
                    ias_fmp_onnet_wireline_list_mod = self.modify_zero_month_year(ias_fmp_onnet_wireline_list)
                    # ias_fmp_onnet_wireline_list.sort(key = lambda date: datetime.strptime(date[1], '%b-%Y')) 
                    
                if (label_name == "IAS-FMP-onnet-wireless"):
                    ias_fmp_onnet_wireless_list.append((label_name, year_name, count))
                    # ias_fmp_onnet_wireless_list.sort(key = lambda date: datetime.strptime(date[1], '%b-%Y'))
                    ias_fmp_onnet_wireless_list_mod = self.modify_zero_month_year(ias_fmp_onnet_wireless_list)

                if (label_name == "IAS-FMP-offnet-wireless"):
                    ias_fmp_offnet_wireless_list.append((label_name, year_name, count))
                    ias_fmp_offnet_wireless_list_mod = self.modify_zero_month_year(ias_fmp_offnet_wireless_list)
                    # ias_fmp_offnet_wireless_list.sort(key = lambda date: datetime.strptime(date[1], '%b-%Y'))
                
                if (label_name == "IAS-FP-onnet-wireline"):
                    ias_fp_onnet_wireline_list.append((label_name, year_name, count))
                    # ias_fp_onnet_wireline_list.sort(key = lambda date: datetime.strptime(date[1], '%b-%Y'))
                    ias_fp_onnet_wireline_list_mod = self.modify_zero_month_year(ias_fp_onnet_wireline_list)

                if (label_name == "IAS-MFMP-offnet-wireless"):
                    ias_mfmp_offnet_wireless_list.append((label_name, year_name, count))
                    # ias_mfmp_offnet_wireless_list.sort(key = lambda date: datetime.strptime(date[1], '%b-%Y'))
                    ias_mfmp_offnet_wireless_list_mod = self.modify_zero_month_year(ias_mfmp_offnet_wireless_list)
                
                if (label_name == "IAS-MFMP-onnet-wireline"):
                    ias_mfmp_onnet_wireline_list.append((label_name, year_name, count))
                    # ias_mfmp_onnet_wireline_list.sort(key = lambda date: datetime.strptime(date[1], '%b-%Y'))
                    ias_mfmp_onnet_wireline_list_mod = self.modify_zero_month_year(ias_mfmp_onnet_wireline_list)

                if (label_name == "IAS-MFMP-onnet-wireless"):
                    ias_mfmp_onnet_wireless_list.append((label_name, year_name, count))
                    # ias_mfmp_onnet_wireless_list.sort(key = lambda date: datetime.strptime(date[1], '%b-%Y'))
                    ias_mfmp_onnet_wireless_list_mod = self.modify_zero_month_year(ias_mfmp_onnet_wireless_list)

                if (label_name == "GVPN-FP-onnet-wireless"):
                    gvpn_fp_onnet_wireless_list.append((label_name, year_name, count))
                    # gvpn_fp_onnet_wireless_list.sort(key = lambda date: datetime.strptime(date[1], '%b-%Y'))
                    gvpn_fp_onnet_wireless_list_mod = self.modify_zero_month_year(gvpn_fp_onnet_wireless_list)

                if (label_name == "GVPN-FMP-onnet-wireline"):
                    gvpn_fmp_onnet_wireline_list.append((label_name, year_name, count))
                    # gvpn_fmp_onnet_wireline_list.sort(key = lambda date: datetime.strptime(date[1], '%b-%Y'))
                    gvpn_fmp_onnet_wireline_list_mod = self.modify_zero_month_year(gvpn_fmp_onnet_wireline_list)

                if (label_name == "GVPN-MFMP-onnet-wireline"):
                    gvpn_mfmp_onnet_wireline_list.append((label_name, year_name, count))
                    # gvpn_mfmp_onnet_wireline_list.sort(key = lambda date: datetime.strptime(date[1], '%b-%Y'))
                    gvpn_mfmp_onnet_wireline_list_mod = self.modify_zero_month_year(gvpn_mfmp_onnet_wireline_list)
           
            
        chrono_list.sort(key = lambda date: datetime.strptime(date[1], '%b-%Y')) 
        sorted_year_list = sorted(year_list)
        
        return ias_fmp_onnet_wireline_list_mod, ias_fmp_onnet_wireless_list_mod,\
        ias_fmp_offnet_wireless_list_mod, ias_fp_onnet_wireline_list_mod,\
        ias_mfmp_offnet_wireless_list_mod, ias_mfmp_onnet_wireless_list_mod, ias_mfmp_onnet_wireline_list_mod, \
        gvpn_fp_onnet_wireless_list_mod, gvpn_fmp_onnet_wireline_list_mod, gvpn_mfmp_onnet_wireline_list_mod
        
    def get_chart_6_content(self):
        '''Returns the chart 6 content
        '''
        ias_fmp_onnet_wireline_cnt_list, ias_fmp_onnet_wireless_cnt_list,\
        ias_fmp_offnet_wireless_cnt_list, ias_fp_onnet_wireline_cnt_list,\
        ias_mfmp_offnet_wireless_cnt_list, ias_mfmp_onnet_wireless_cnt_list, ias_mfmp_onnet_wireline_cnt_list, \
        gvpn_fp_onnet_wireless_cnt_list, gvpn_fmp_onnet_wireline_cnt_list, gvpn_mfmp_onnet_wireline_cnt_list = self.get_chronological_data()
        
        chart_6_name = "Overall F & P Timeline report"
        chart_content = "" + TE.chart_template_six
        chart_6_id = "chart_6"
        
        c6_row_labels = ["Aug-2018", "Sep-2018", "Oct-2018", "Nov-2018", "Dec-2018", "Jan-2019", "Feb-2019", "Mar-2019", "Apr-2019", "May-2019", "Jun-2019"]

        label_1_name = "IAS-FMP-onnet-wireline"
        label_2_name = "IAS-FMP-onnet-wireless"
        label_3_name = "IAS-FMP-offnet-wireless"
        label_4_name = "IAS-FP-onnet-wireline"
        label_5_name = "IAS-MFMP-offnet-wireless"
        label_6_name = "IAS-MFMP-onnet-wireless"
        label_7_name = "IAS-MFMP-onnet-wireline"
        label_8_name = "GVPN-FP-onnet-wireless"
        label_9_name = "GVPN-FMP-onnet-wireline"
        label_10_name = "GVPN-MFMP-onnet-wireline"
    
        fp6_chart_content = chart_content%(chart_6_name, chart_6_id, c6_row_labels, 
                                           ias_fmp_onnet_wireline_cnt_list, ias_fmp_onnet_wireless_cnt_list, \
                                           ias_fmp_offnet_wireless_cnt_list, ias_fp_onnet_wireline_cnt_list, \
                                           ias_mfmp_offnet_wireless_cnt_list, ias_mfmp_onnet_wireless_cnt_list, \
                                           ias_mfmp_onnet_wireline_cnt_list, gvpn_fp_onnet_wireless_cnt_list, \
                                           gvpn_fmp_onnet_wireline_cnt_list, gvpn_mfmp_onnet_wireline_cnt_list, \
                                           chart_6_id, label_1_name, label_2_name, label_3_name, label_4_name, label_5_name, \
                                           label_6_name, label_7_name, label_8_name, label_9_name, label_10_name)
        return fp6_chart_content
    
    def get_chart_7_content(self):
        '''Returns the chart 7 content
        '''
        npl_fmp_list, npl_fp_list, npl_mfmp_list, npl_mfp_list = self.get_npl_data()
    
        c7_row_labels = ["Aug-2018", "Sep-2018", "Oct-2018", "Nov-2018", "Dec-2018", "Jan-2019", "Feb-2019", "Mar-2019", "Apr-2019", "May-2019", "Jun-2019"]

        chart_7_name = "Overall F & P Timeline report for NPL"
        chart_content = "" + TE.chart_template_seven
        chart_7_id = "chart_7"
        
        label_1_name = "NPL-FMP"
        label_2_name = "NPL-FP"
        label_3_name = "NPL-MFMP"
        label_4_name = "NPL-MFP"
        
        fp7_chart_content = chart_content%(chart_7_name, chart_7_id, c7_row_labels, 
                                           npl_fmp_list, npl_fp_list, \
                                           npl_mfmp_list, npl_mfp_list, chart_7_id, label_1_name, label_2_name, label_3_name, label_4_name)
        
        
        return fp7_chart_content
    
    def get_chart_0_site_level_content(self):
        '''Returns the chart 0 site level HTML content
        '''
        price_list, prod_list, fmp_list, mfmp_list, fp_list, mfp_list, prod_dict = self.get_site_level_content()
        c0_row_labels = prod_list
        c0_fmp = fmp_list
        c0_mfmp = mfmp_list
        c0_fp = fp_list
        c0_mfp = mfp_list
        pivot_dict = prod_dict
        
        chart_content = "" + TE.chart_template_four
        chart_0_id = "chart_0"
        chart_0_name = "Feasibility Price Status Summary based on site level"
        label_1_name = "Zero touch feasibility; Zero touch pricing(FP)"
        label_2_name = "Manual pricing; Zero touch feasibility(FMP)"
        label_3_name = "Zero touch pricing; manual feasibility (MFP)"
        label_4_name = "Manual pricing; Manual feasibility (MFMP)"
        
        fp_chart_content = chart_content%(chart_0_name, chart_0_id, c0_row_labels, c0_fp, c0_fmp, c0_mfp, c0_mfmp, chart_0_id, label_1_name, label_2_name, label_3_name, label_4_name)
        return fp_chart_content
    
    
    def get_chart_01_order_level_content(self):
        '''Returns the chart 01 order level content
        '''
        #Based on order level
        
        order_prod_list, order_fmp_list, order_mfmp_list, order_fp_list, order_mfp_list = self.get_order_level_content()
        c01_row_labels = order_prod_list
        c01_fmp = order_fmp_list
        c01_mfmp = order_mfmp_list
        c01_fp = order_fp_list
        c01_mfp = order_mfp_list
        
        chart_content = "" + TE.chart_template_four
        chart_01_id = "chart_01"
        chart_01_name = "Feasibility Price Status Summary based on order level"
        label_1_name = "Zero touch feasibility; Zero touch pricing(FP)"
        label_2_name = "Manual pricing; Zero touch feasibility(FMP)"
        label_3_name = "Zero touch pricing; manual feasibility (MFP)"
        label_4_name = "Manual pricing; Manual feasibility (MFMP)"

        fp01_chart_content = chart_content%(chart_01_name, chart_01_id, c01_row_labels, c01_fp, c01_fmp, c01_mfp, c01_mfmp, chart_01_id, label_1_name, label_2_name, label_3_name, label_4_name)
        return fp01_chart_content
    
    
    def get_chart_1_content(self):
        '''Returns the chart 1 content
        '''
        price_list, prod_list, fmp_list, mfmp_list, fp_list, mfp_list, prod_dict = self.get_site_level_content()
        c1_row_labels = ["Manual pricing; manual feasibility",
                  "Manual pricing; zero touch feasibility",
                  "Zero touch pricing; manual feasibility",
                  "Zero touch pricing; zero touch feasibility"]
        c1_ias = list(price_list[0])
        c1_gvpn = list(price_list[1])
        c1_npl = list(price_list[2])
        
        chart_content = "" + TE.chart_template_three_6
        chart_1_id = "chart_1"
        chart_1_name = "Pricing and Feasibility Summary based on product level"
        label_1_name = "IAS"
        label_2_name = "NPL"
        label_3_name = "GVPN"
        fp1_chart_content = chart_content % (chart_1_name, chart_1_id, c1_row_labels, c1_ias, c1_npl, c1_gvpn, chart_1_id, label_1_name, label_2_name, label_3_name)
        return fp1_chart_content
    
    
    def get_chart_2_content(self):
        '''Returns the chart 2 content based on deviation slab content
        '''
        # Based on deviation slab level content
        arc_dev_list, nrc_dev_list, acv_dev_list = self.get_deviation_slab_level_content()
        # c2_row_labels = ["<(100)%","<(50-100)%","<(15-50)%", "<(5-15)%", "(0-5)%", ">(5-15)%", ">(15-50)%", ">(50-100)%", ">(100)%"];
        # c2_row_labels =  ['>(0-5)%', '>(100)%', '>(15-50)%', '<(15-50)%', '<(0-5)%', '>(5-15)%', '<(5-15)%', '>(50-100)%', '<(50-100)%']
        c2_row_labels =  ['>(100)%', '>(50-100)%', '>(15-50)%', '>(5-15)%', '>(0-5)%', '<(0-5)%', '<(5-15)%', '<(15-50)%', '<(50-100)%']

        c2_acv = acv_dev_list
        c2_arc = arc_dev_list
        c2_nrc = nrc_dev_list
        
        chart_content = "" + TE.chart_template_three
        chart_2_id = "chart_2"
        chart_2_name = "Overall universe spread – ACV, ARC, NRC"
        label_1_name = "ACV"
        label_2_name = "ARC"
        label_3_name = "NRC"
        fp2_chart_content = chart_content % (chart_2_name, chart_2_id, c2_row_labels, c2_acv, c2_arc, c2_nrc, chart_2_id, label_1_name, label_2_name, label_3_name)
        return fp2_chart_content
    
    
    def get_chart_3_content(self):
        '''Returns the chart 3 content based on component level
        '''
        # Based on component level
        c3_row_labels = ["Port","Last Mile","CPE"]
        arc_list, nrc_list =  self.get_component_level_content()

        c3_arc = [218, 29, 51]
        c3_nrc = [18, 44, 19]
        
        # c3_arc = arc_list
        # c3_nrc = nrc_list
        
        chart_content = "" + TE.chart_template
        chart_3_id = "chart_3"
        chart_3_name = "Deviation between Optimus and Actual Price (Based on Component Level)"
        label_1_name = "ARC"
        label_2_name = "NRC"
        fp3_chart_content = chart_content % (chart_3_name, chart_3_id, c3_row_labels, c3_arc, c3_nrc, chart_3_id, label_1_name, label_2_name)
        return fp3_chart_content
    
    
    def get_chart_4_content(self):
        '''Returns the chart 4 content (pie)
        '''        
        # Pie chart
        c4_row_labels = ["Reason1","Reason2","Reason3", "Reason4"]
        c4_arc = [20, 30, 40, 10]
        
        chart_content = "" + TE.pie_chart_template
        chart_5_id = "chart_5"
        chart_5_name = "Reasons for manual pricing – TBD, Once CHANGES are INCLUDED IN REPORT and OMS"
        label_1_name = "ARC"
        fp5_chart_content = chart_content % (chart_5_name, chart_5_id, c4_row_labels, c4_arc, chart_5_id, label_1_name)
        return fp5_chart_content
            
            
    def write_to_html(self):
        '''Writes the generated content to HTML
        '''    
        header = " "
        html_title = "Pivot Table"
        header += TE.content_header.format(html_title)
        with open("index.html", "w") as fhandle:
            fhandle.write(header)
            
            # FP status table
            table_title_row = TE.table_title_row
            fhandle.write(table_title_row)

            fhandle.write(self.get_row_content())

            # MRC deviation share table
            sub_table = TE.sec_table_col
            fhandle.write(sub_table)

            table_content = ""
            sec_table_content = table_content + TE.table_content
            fhandle.write(sec_table_content)

            sub_table_title_row = TE.sub_table_title_row
            fhandle.write(sub_table_title_row)

            fhandle.write(self.get_sub_row_content())

            # FP status summary based on site level
            fp_chart_content = self.get_chart_0_site_level_content()
            fhandle.write(fp_chart_content)
          
            # FP status summary based on order level
            fp01_chart_content = self.get_chart_01_order_level_content()
            fhandle.write(fp01_chart_content)
            
            # Pricing and Feasibility Summary based on product level
            # fp1_chart_content = self.get_chart_1_content()
            # fhandle.write(fp1_chart_content)

            # Based on deviation slab content
            fp2_chart_content = self.get_chart_2_content()
            fhandle.write(fp2_chart_content)
            
            # Pricing and Feasibility Summary based on product level
            fp1_chart_content = self.get_chart_1_content()
            fhandle.write(fp1_chart_content)

            # Based on component level
            fp3_chart_content = self.get_chart_3_content()
            fhandle.write(fp3_chart_content)
            
            # Pie chart
            # fp5_content = self.get_chart_5_content()
            # fhandle.write(fp5_chart_content)
            
            fp6_chart_content = self.get_chart_6_content()
            fhandle.write(fp6_chart_content)
            
            fp7_chart_content = self.get_chart_7_content()
            fhandle.write(fp7_chart_content)
            
            # Footer text
            recipe_footer = TE.footer_text
            fhandle.write(recipe_footer)
            
            print("Successfully generated the Feasibility and Pricing Dashboard....... ")
            print(os.getcwd())


spg = SamplePivotGenerator()
spg.write_to_html()
db.close()
