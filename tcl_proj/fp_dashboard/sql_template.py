#!/usr/bin/env python
'''*************************************************************************************************
@summary  : SQL template for Pivot table and graph generation
@author   : Aparna Rao Kota
@since    : 2019-July
*************************************************************************************************'''
import sys
import os


class SqlTemplate(object):
    '''
        Contains SQL template that collects data from DB
    '''

    # ===========================================================================
    # Query based on Order level
    # ===========================================================================
    sel_1_cmd = """select product_name,
    FP,(FP/total_orders)*100 as FP_percent,
    FMP,(FMP/total_orders)*100 as FMP_percent,
    MFP,(MFP/total_orders)*100 as MFP_percent,
    MFMP,(MFMP/total_orders)*100 as MFMP_percent,
    total_orders
    from(select product_name,coalesce(FP,0) as FP,coalesce(FMP,0) as FMP,coalesce(MFP,0) as MFP,coalesce(MFMP,0) as MFMP,
    sum(coalesce(FP,0)+coalesce(FMP,0)+coalesce(MFP,0)+coalesce(MFMP,0)) as total_orders
    from
    (select product_name,sum(FP) as FP,sum(FMP) as FMP,sum(MFP) as MFP,sum(MFMP) as MFMP
    from
    (select product_name,
    case when fp_status = 'FP' then counts end as FP,
    case when fp_status = 'FMP' then counts end as FMP,
    case when fp_status = 'MFP' then counts end as MFP,
    case when fp_status = 'MFMP' then counts end as MFMP
    from (select product_name,fp_status,count(distinct order_code) as counts
    from oms.vw_order_vs_pe_rcmd_site_cmp_20190627
    where is_selected = 1
    and product_name_fsbility is not null
    group by product_name,fp_status) X
    )Y
    group by product_name
    )Z
    group by product_name
    )A
    """

    # =================================================================================
    # Query based on site level
    # =================================================================================
    sel_2_cmd = """select product_name,
    FP,(FP/total_sites)*100 as FP_percent,
    FMP,(FMP/total_sites)*100 as FMP_percent,
    MFP,(MFP/total_sites)*100 as MFP_percent,
    MFMP,(MFMP/total_sites)*100 as MFMP_percent,
    total_sites
    from(select product_name,coalesce(FP,0) as FP,coalesce(FMP,0) as FMP,coalesce(MFP,0) as MFP,coalesce(MFMP,0) as MFMP,
    sum(coalesce(FP,0)+coalesce(FMP,0)+coalesce(MFP,0)+coalesce(MFMP,0)) as total_sites
    from
    (select product_name,sum(FP) as FP,sum(FMP) as FMP,sum(MFP) as MFP,sum(MFMP) as MFMP
    from
    (select product_name,
    case when fp_status = 'FP' then counts end as FP,
    case when fp_status = 'FMP' then counts end as FMP,
    case when fp_status = 'MFP' then counts end as MFP,
    case when fp_status = 'MFMP' then counts end as MFMP
    from 
    (select 
    case 
    when product_name in ('Managed Single Internet Access','Single Internet Access') then 'IAS'
    when product_name in ('Single managed GVPN','Single Unmanaged GVPN') then 'GVPN'
    end as product_name
    ,fp_status,count(distinct site_code) as counts
    from oms.vw_order_vs_pe_rcmd_site_cmp_20190627
    where is_selected = 1
    and product_name_fsbility is not null
    and product_name in ('Managed Single Internet Access','Single Internet Access','Single managed GVPN','Single Unmanaged GVPN')
    group by product_name,fp_status) X
    )Y
    group by product_name
    )Z
    group by product_name
    )A

    union

    select product_name,
    FP,(FP/total_sites)*100 as FP_percent,
    FMP,(FMP/total_sites)*100 as FMP_percent,
    MFP,(MFP/total_sites)*100 as MFP_percent,
    MFMP,(MFMP/total_sites)*100 as MFMP_percent,
    total_sites
    from(select product_name,coalesce(FP,0) as FP,coalesce(FMP,0) as FMP,coalesce(MFP,0) as MFP,coalesce(MFMP,0) as MFMP,
    sum(coalesce(FP,0)+coalesce(FMP,0)+coalesce(MFP,0)+coalesce(MFMP,0)) as total_sites
    from
    (select product_name,sum(FP) as FP,sum(FMP) as FMP,sum(MFP) as MFP,sum(MFMP) as MFMP
    from
    (select product_name,
    case when fp_status = 'FP' then counts end as FP,
    case when fp_status = 'FMP' then counts end as FMP,
    case when fp_status = 'MFP' then counts end as MFP,
    case when fp_status = 'MFMP' then counts end as MFMP
    from 
    (select 
    'NPL' as product_name
    ,A.fp_status,count(distinct C.link_code)as counts
    from oms.vw_order_vs_pe_rcmd_site_cmp_20190627 A
    left outer join oms.order_ill_sites B
    on A.site_code = B.site_code
    left outer join oms.order_npl_link C
    on (B.id = C.site_A_id 
    or B.id = C.site_B_id)
    where is_selected = 1
    and product_name_fsbility is not null
    and product_name in ('Private Line - NPL')
    group by product_name,fp_status) X
    )Y
    group by product_name
    )Z
    group by product_name
    )A
    """

    # =================================================================================
    # Contains based on deviation slab
    # =================================================================================

    sel_3_cmd = """with cte_table
    as (select site_code,fp_status,
    case 
    when Delta_ARC < -100 then '>100%-Under'
    when Delta_ARC <= -50 and Delta_ARC >= -100 then 'i_50-100%-Under'
    when Delta_ARC <=-15 and Delta_ARC > -50 then 'h_15-50%-Under'
    when Delta_ARC <=-5 and Delta_ARC > -15 then 'g_5-15%-Under'
    when Delta_ARC <0 and Delta_ARC > -5 then 'f_5-0%-Under'
    when Delta_ARC >=0 and Delta_ARC < 5 then 'e_0-5%-Over'
    when Delta_ARC >=5 and Delta_ARC < 15 then 'd_5-15%-Over'
    when Delta_ARC >=15 and Delta_ARC < 50 then 'c_15-50%-Over'
    when Delta_ARC >=50 and Delta_ARC <= 100 then 'b_50-100%-Over'
    when Delta_ARC > 100 then 'a_100%-Over' 
    else 'Error' 
    end as ARC_Deviation_slab,
    case 
    when Delta_NRC < -100 then '>100%-Under'
    when Delta_NRC <= -50 and Delta_NRC >= -100 then 'i_50-100%-Under'
    when Delta_NRC <=-15 and Delta_NRC > -50 then 'h_15-50%-Under'
    when Delta_NRC <=-5 and Delta_NRC > -15 then 'g_5-15%-Under'
    when Delta_NRC <0 and Delta_NRC > -5 then 'f_5-0%-Under'
    when Delta_NRC >=0 and Delta_NRC < 5 then 'e_0-5%-Over'
    when Delta_NRC >=5 and Delta_NRC < 15 then 'd_5-15%-Over'
    when Delta_NRC >=15 and Delta_NRC < 50 then 'c_15-50%-Over'
    when Delta_NRC >=50 and Delta_NRC <= 100 then 'b_50-100%-Over'
    when Delta_NRC > 100 then 'a_100%-Over' 
    else 'Error'
    end as NRC_Deviation_slab,
    case 
    when Delta_ACV < -100 then '>100%-Under'
    when Delta_ACV <= -50 and Delta_ACV >= -100 then 'i_50-100%-Under'
    when Delta_ACV <=-15 and Delta_ACV > -50 then 'h_15-50%-Under'
    when Delta_ACV <=-5 and Delta_ACV > -15 then 'g_5-15%-Under'
    when Delta_ACV <0 and Delta_ACV > -5 then 'f_5-0%-Under'
    when Delta_ACV >=0 and Delta_ACV < 5 then 'e_0-5%-Over'
    when Delta_ACV >=5 and Delta_ACV < 15 then 'd_5-15%-Over'
    when Delta_ACV >=15 and Delta_ACV < 50 then 'c_15-50%-Over'
    when Delta_ACV >=50 and Delta_ACV <= 100 then 'b_50-100%-Over'
    when Delta_ACV > 100 then 'a_100%-Over' 
    else 'Error'
    end as ACV_Deviation_slab
    from 
    (select site_code,fp_status,Optimus_ARC,Actual_ARC,Optimus_NRC,Actual_NRC,Optimus_ACV,Actual_ACV,
    case 
    when Actual_ARC = 0 then 100
    else ((Optimus_ARC/Actual_ARC) - 1)*100 end as Delta_ARC,
    case 
    when Actual_NRC = 0 then 100
    else ((Optimus_NRC/Actual_NRC) - 1)*100 end as Delta_NRC,
    case 
    when Actual_ACV = 0 then 100
    else ((Optimus_ACV/Actual_ACV) - 1)*100 end as Delta_ACV
    from
    (select site_code,fp_status,
    coalesce(Optimus_ARC,0) as Optimus_ARC,coalesce(Optimus_NRC,0) as Optimus_NRC,
    coalesce(Actual_ARC,0) as Actual_ARC,coalesce(Actual_NRC,0) as Actual_NRC,
    coalesce(Optimus_ARC,0) + coalesce(Optimus_NRC,0) as Optimus_ACV,
    coalesce(Actual_ARC,0)  + coalesce(Actual_NRC,0) as Actual_ACV
    from oms.vw_order_vs_pe_rcmd_site_cmp_20190627
    where product_name in ('Managed Single Internet Access','Single Internet Access','Single managed GVPN','Single Unmanaged GVPN')
    and Is_Selected = 1

    union

    select distinct C.link_code,A.fp_status,
    coalesce(A.Optimus_ARC,0) as Optimus_ARC,coalesce(A.Optimus_NRC,0) as Optimus_NRC,
    coalesce(A.Actual_ARC,0) as Actual_ARC,coalesce(A.Actual_NRC,0) as Actual_NRC,
    coalesce(A.Optimus_ARC,0) + coalesce(A.Optimus_NRC,0) as Optimus_ACV,
    coalesce(A.Actual_ARC,0)  + coalesce(A.Actual_NRC,0) as Actual_ACV
    from oms.vw_order_vs_pe_rcmd_site_cmp_20190627 A
    left outer join oms.order_ill_sites B
    on A.site_code = B.site_code
    left outer join oms.order_npl_link C
    on (B.id = C.site_A_id 
    or B.id = C.site_B_id)
    where A.is_selected = 1
    and A.product_name_fsbility is not null
    and A.product_name in ('Private Line - NPL')
    )X
    )Y
    )
    select 'ARC' as Deviation_Type,ARC_Deviation_slab as Slab_Value,
    FP,(FP/total_sites)*100 as FP_percent,
    FMP,(FMP/total_sites)*100 as FMP_percent,
    MFP,(MFP/total_sites)*100 as MFP_percent,
    MFMP,(MFMP/total_sites)*100 as MFMP_percent,
    total_sites
    from
    (select ARC_Deviation_slab,coalesce(FP,0) as FP,coalesce(FMP,0) as FMP,coalesce(MFP,0) as MFP,coalesce(MFMP,0) as MFMP,
    sum(coalesce(FP,0)+coalesce(FMP,0)+coalesce(MFP,0)+coalesce(MFMP,0)) as total_sites
    from
    (select ARC_Deviation_slab,sum(FP) as FP,sum(FMP) as FMP,sum(MFP) as MFP,sum(MFMP) as MFMP
    from
    (select ARC_Deviation_slab,
    case when fp_status = 'FP' then counts end as FP,
    case when fp_status = 'FMP' then counts end as FMP,
    case when fp_status = 'MFP' then counts end as MFP,
    case when fp_status = 'MFMP' then counts end as MFMP
    from
    (select ARC_Deviation_slab,fp_status,count(site_code) as counts
    from cte_table
    group by ARC_Deviation_slab,fp_status)XX
    )YY
    group by ARC_Deviation_slab
    )ZZ
    group by ARC_Deviation_slab
    )AA

    union

    select 'NRC' as Deviation_Type,NRC_Deviation_slab as Slab_Value,
    FP,(FP/total_sites)*100 as FP_percent,
    FMP,(FMP/total_sites)*100 as FMP_percent,
    MFP,(MFP/total_sites)*100 as MFP_percent,
    MFMP,(MFMP/total_sites)*100 as MFMP_percent,
    total_sites
    from
    (select NRC_Deviation_slab,coalesce(FP,0) as FP,coalesce(FMP,0) as FMP,coalesce(MFP,0) as MFP,coalesce(MFMP,0) as MFMP,
    sum(coalesce(FP,0)+coalesce(FMP,0)+coalesce(MFP,0)+coalesce(MFMP,0)) as total_sites
    from
    (select NRC_Deviation_slab,sum(FP) as FP,sum(FMP) as FMP,sum(MFP) as MFP,sum(MFMP) as MFMP
    from
    (select NRC_Deviation_slab,
    case when fp_status = 'FP' then counts end as FP,
    case when fp_status = 'FMP' then counts end as FMP,
    case when fp_status = 'MFP' then counts end as MFP,
    case when fp_status = 'MFMP' then counts end as MFMP
    from
    (select NRC_Deviation_slab,fp_status,count(site_code) as counts
    from cte_table
    group by NRC_Deviation_slab,fp_status)XX
    )YY
    group by NRC_Deviation_slab
    )ZZ
    group by NRC_Deviation_slab
    )AA

    union

    select 'ACV' as Deviation_Type,ACV_Deviation_slab as Slab_Value,
    FP,(FP/total_sites)*100 as FP_percent,
    FMP,(FMP/total_sites)*100 as FMP_percent,
    MFP,(MFP/total_sites)*100 as MFP_percent,
    MFMP,(MFMP/total_sites)*100 as MFMP_percent,
    total_sites
    from
    (select ACV_Deviation_slab,coalesce(FP,0) as FP,coalesce(FMP,0) as FMP,coalesce(MFP,0) as MFP,coalesce(MFMP,0) as MFMP,
    sum(coalesce(FP,0)+coalesce(FMP,0)+coalesce(MFP,0)+coalesce(MFMP,0)) as total_sites
    from
    (select ACV_Deviation_slab,sum(FP) as FP,sum(FMP) as FMP,sum(MFP) as MFP,sum(MFMP) as MFMP
    from
    (select ACV_Deviation_slab,
    case when fp_status = 'FP' then counts end as FP,
    case when fp_status = 'FMP' then counts end as FMP,
    case when fp_status = 'MFP' then counts end as MFP,
    case when fp_status = 'MFMP' then counts end as MFMP
    from
    (select ACV_Deviation_slab,fp_status,count(site_code) as counts
    from cte_table
    group by ACV_Deviation_slab,fp_status)XX
    )YY
    group by ACV_Deviation_slab
    )ZZ
    group by ACV_Deviation_slab
    )AA
    """
    
   # =================================================================================
    # Contains based on deviation slab
    # =================================================================================

    sel_4_cmd = """with cte_table
    as (select site_code,fp_status,
    case 
    when Delta_ARC < -100 then '>100%-Under'
    when Delta_ARC <= -50 and Delta_ARC >= -100 then '<(50-100)%'
    when Delta_ARC <=-15 and Delta_ARC > -50 then '<(15-50)%'
    when Delta_ARC <=-5 and Delta_ARC > -15 then '<(5-15)%'
    when Delta_ARC <0 and Delta_ARC > -5 then '<(5-0)%'
    when Delta_ARC >=0 and Delta_ARC < 5 then '>(0-5)%'
    when Delta_ARC >=5 and Delta_ARC < 15 then '>(5-15)%'
    when Delta_ARC >=15 and Delta_ARC < 50 then '>(15-50)%'
    when Delta_ARC >=50 and Delta_ARC <= 100 then '>(50-100)%'
    when Delta_ARC > 100 then '>100%-Over' 
    else 'Error' 
    end as ARC_Deviation_slab,
    case 
    when Delta_NRC < -100 then '>100%-Under'
    when Delta_NRC <= -50 and Delta_NRC >= -100 then '<(50-100)%'
    when Delta_NRC <=-15 and Delta_NRC > -50 then '<(15-50)%'
    when Delta_NRC <=-5 and Delta_NRC > -15 then '<(5-15)%'
    when Delta_NRC <0 and Delta_NRC > -5 then '<(5-0)%'
    when Delta_NRC >=0 and Delta_NRC < 5 then '>(0-5)%'
    when Delta_NRC >=5 and Delta_NRC < 15 then '>(5-15)%'
    when Delta_NRC >=15 and Delta_NRC < 50 then '>(15-50)'
    when Delta_NRC >=50 and Delta_NRC <= 100 then '>(50-100)'
    when Delta_NRC > 100 then '>100%-Over' 
    else 'Error'
    end as NRC_Deviation_slab,
    case 
    when Delta_ACV < -100 then '>100%-Under'
    when Delta_ACV <= -50 and Delta_ACV >= -100 then '<(50-100)%'
    when Delta_ACV <=-15 and Delta_ACV > -50 then '<(15-50)%'
    when Delta_ACV <=-5 and Delta_ACV > -15 then '<(5-15)%'
    when Delta_ACV <0 and Delta_ACV > -5 then '<(5-0)%'
    when Delta_ACV >=0 and Delta_ACV < 5 then '>(0-5)%'
    when Delta_ACV >=5 and Delta_ACV < 15 then '>(5-15)%'
    when Delta_ACV >=15 and Delta_ACV < 50 then '>(15-50)%'
    when Delta_ACV >=50 and Delta_ACV <= 100 then '>(50-100)%'
    when Delta_ACV > 100 then '>100%-Over' 
    else 'Error'
    end as ACV_Deviation_slab
    from 
    (select site_code,fp_status,Optimus_ARC,Actual_ARC,Optimus_NRC,Actual_NRC,Optimus_ACV,Actual_ACV,
    case 
    when Actual_ARC = 0 then 100
    else ((Optimus_ARC/Actual_ARC) - 1)*100 end as Delta_ARC,
    case 
    when Actual_NRC = 0 then 100
    else ((Optimus_NRC/Actual_NRC) - 1)*100 end as Delta_NRC,
    case 
    when Actual_ACV = 0 then 100
    else ((Optimus_ACV/Actual_ACV) - 1)*100 end as Delta_ACV
    from
    (select site_code,fp_status,
    coalesce(Optimus_ARC,0) as Optimus_ARC,coalesce(Optimus_NRC,0) as Optimus_NRC,
    coalesce(Actual_ARC,0) as Actual_ARC,coalesce(Actual_NRC,0) as Actual_NRC,
    coalesce(Optimus_ARC,0) + coalesce(Optimus_NRC,0) as Optimus_ACV,
    coalesce(Actual_ARC,0)  + coalesce(Actual_NRC,0) as Actual_ACV
    from oms.vw_order_vs_pe_rcmd_site_cmp_20190627
    where product_name in ('Managed Single Internet Access','Single Internet Access','Single managed GVPN','Single Unmanaged GVPN')
    and Is_Selected = 1

    union

    select distinct C.link_code,A.fp_status,
    coalesce(A.Optimus_ARC,0) as Optimus_ARC,coalesce(A.Optimus_NRC,0) as Optimus_NRC,
    coalesce(A.Actual_ARC,0) as Actual_ARC,coalesce(A.Actual_NRC,0) as Actual_NRC,
    coalesce(A.Optimus_ARC,0) + coalesce(A.Optimus_NRC,0) as Optimus_ACV,
    coalesce(A.Actual_ARC,0)  + coalesce(A.Actual_NRC,0) as Actual_ACV
    from oms.vw_order_vs_pe_rcmd_site_cmp_20190627 A
    left outer join oms.order_ill_sites B
    on A.site_code = B.site_code
    left outer join oms.order_npl_link C
    on (B.id = C.site_A_id 
    or B.id = C.site_B_id)
    where A.is_selected = 1
    and A.product_name_fsbility is not null
    and A.product_name in ('Private Line - NPL')
    )X
    )Y
    )
    select 'ARC' as Deviation_Type,ARC_Deviation_slab as Slab_Value,
    FP,(FP/total_sites)*100 as FP_percent,
    FMP,(FMP/total_sites)*100 as FMP_percent,
    MFP,(MFP/total_sites)*100 as MFP_percent,
    MFMP,(MFMP/total_sites)*100 as MFMP_percent,
    total_sites
    from
    (select ARC_Deviation_slab,coalesce(FP,0) as FP,coalesce(FMP,0) as FMP,coalesce(MFP,0) as MFP,coalesce(MFMP,0) as MFMP,
    sum(coalesce(FP,0)+coalesce(FMP,0)+coalesce(MFP,0)+coalesce(MFMP,0)) as total_sites
    from
    (select ARC_Deviation_slab,sum(FP) as FP,sum(FMP) as FMP,sum(MFP) as MFP,sum(MFMP) as MFMP
    from
    (select ARC_Deviation_slab,
    case when fp_status = 'FP' then counts end as FP,
    case when fp_status = 'FMP' then counts end as FMP,
    case when fp_status = 'MFP' then counts end as MFP,
    case when fp_status = 'MFMP' then counts end as MFMP
    from
    (select ARC_Deviation_slab,fp_status,count(site_code) as counts
    from cte_table
    group by ARC_Deviation_slab,fp_status)XX
    )YY
    group by ARC_Deviation_slab
    )ZZ
    group by ARC_Deviation_slab
    )AA

    union

    select 'NRC' as Deviation_Type,NRC_Deviation_slab as Slab_Value,
    FP,(FP/total_sites)*100 as FP_percent,
    FMP,(FMP/total_sites)*100 as FMP_percent,
    MFP,(MFP/total_sites)*100 as MFP_percent,
    MFMP,(MFMP/total_sites)*100 as MFMP_percent,
    total_sites
    from
    (select NRC_Deviation_slab,coalesce(FP,0) as FP,coalesce(FMP,0) as FMP,coalesce(MFP,0) as MFP,coalesce(MFMP,0) as MFMP,
    sum(coalesce(FP,0)+coalesce(FMP,0)+coalesce(MFP,0)+coalesce(MFMP,0)) as total_sites
    from
    (select NRC_Deviation_slab,sum(FP) as FP,sum(FMP) as FMP,sum(MFP) as MFP,sum(MFMP) as MFMP
    from
    (select NRC_Deviation_slab,
    case when fp_status = 'FP' then counts end as FP,
    case when fp_status = 'FMP' then counts end as FMP,
    case when fp_status = 'MFP' then counts end as MFP,
    case when fp_status = 'MFMP' then counts end as MFMP
    from
    (select NRC_Deviation_slab,fp_status,count(site_code) as counts
    from cte_table
    group by NRC_Deviation_slab,fp_status)XX
    )YY
    group by NRC_Deviation_slab
    )ZZ
    group by NRC_Deviation_slab
    )AA

    union

    select 'ACV' as Deviation_Type,ACV_Deviation_slab as Slab_Value,
    FP,(FP/total_sites)*100 as FP_percent,
    FMP,(FMP/total_sites)*100 as FMP_percent,
    MFP,(MFP/total_sites)*100 as MFP_percent,
    MFMP,(MFMP/total_sites)*100 as MFMP_percent,
    total_sites
    from
    (select ACV_Deviation_slab,coalesce(FP,0) as FP,coalesce(FMP,0) as FMP,coalesce(MFP,0) as MFP,coalesce(MFMP,0) as MFMP,
    sum(coalesce(FP,0)+coalesce(FMP,0)+coalesce(MFP,0)+coalesce(MFMP,0)) as total_sites
    from
    (select ACV_Deviation_slab,sum(FP) as FP,sum(FMP) as FMP,sum(MFP) as MFP,sum(MFMP) as MFMP
    from
    (select ACV_Deviation_slab,
    case when fp_status = 'FP' then counts end as FP,
    case when fp_status = 'FMP' then counts end as FMP,
    case when fp_status = 'MFP' then counts end as MFP,
    case when fp_status = 'MFMP' then counts end as MFMP
    from
    (select ACV_Deviation_slab,fp_status,count(site_code) as counts
    from cte_table
    group by ACV_Deviation_slab,fp_status)XX
    )YY
    group by ACV_Deviation_slab
    )ZZ
    group by ACV_Deviation_slab
    )AA
    """
    
    # =================================================================================
    # Contains based on Component Level
    # =================================================================================

    sel_5_cmd = """select sum(cpe_arc_dev) / 1000 as cpe_arc,
                sum(cpe_nrc_dev) / 1000 as cpe_nrc,
                sum(port_arc_dev) / 1000 as port_arc,
                sum(port_nrc_dev) / 1000 as port_nrc,
                sum(last_mile_arc_dev) / 1000 as last_mile_arc,
                sum(last_mile_nrc_dev) / 1000 as last_mile_nrc        
                from
                (select A.product_name, (A.Optimus_CPE_ARC - A.new_actual_cpe_arc) as cpe_arc_dev,
                        (A.Optimus_CPE_NRC - A.new_actual_cpe_nrc) as cpe_nrc_dev,
                        (((A.Optimus_Port_ARC - A.actual_Internet_port_arc) / A.actual_Internet_port_arc) * 100 ) as port_arc_dev, 
                        (((A.Optimus_Port_NRC - A.actual_Internet_port_nrc) / A.actual_Internet_port_nrc)* 100) as port_nrc_dev,
                        (A.Optimus_Last_Mile_Cost_ARC - A.actual_Last_mile_arc) as last_mile_arc_dev, 
                        (A.Optimus_Last_Mile_Cost_NRC - A.actual_Last_mile_nrc) as last_mile_nrc_dev
                from
                (select  distinct site_code, 
                         product_name,
                         actual_Internet_port_arc, 
                         Optimus_Port_ARC,
                         actual_Internet_port_nrc, 
                         Optimus_Port_NRC,
                         actual_Last_mile_arc,
                         Optimus_Last_Mile_Cost_ARC,
                         actual_Last_mile_nrc, 
                         Optimus_Last_Mile_Cost_NRC,
                         Optimus_CPE_ARC, 
                         replace(actual_cpe_arc, 'NULL', 0) as new_actual_cpe_arc,
                         Optimus_CPE_NRC, replace(actual_cpe_arc, 'NULL', 0) as new_actual_cpe_nrc 
                         from oms.vw_order_vs_pe_rcmd_site_cmp_20190627
                         where product_name in ('Managed Single Internet Access','Single Internet Access','Single managed GVPN','Single Unmanaged GVPN') and Is_Selected = 1
                         union
                  select distinct Z.link_code, product_name,
                  actual_Internet_port_arc, 
                  Optimus_Port_ARC,
                  actual_Internet_port_nrc, 
                  Optimus_Port_NRC,
                  actual_Last_mile_arc,
                  Optimus_Last_Mile_Cost_ARC,
                  actual_Last_mile_nrc, 
                  Optimus_Last_Mile_Cost_NRC,
                  Optimus_CPE_ARC, 
                  replace(actual_cpe_arc, 'NULL', 0) as new_actual_cpe_arc,
                  Optimus_CPE_NRC, replace(actual_cpe_arc, 'NULL', 0) as new_actual_cpe_nrc 
                  from oms.vw_order_vs_pe_rcmd_site_cmp_20190627 X
                  left outer join oms.order_ill_sites Y
                  on X.site_code = Y.site_code
                  left outer join oms.order_npl_link Z
                  on (Y.id = Z.site_A_id 
                  or Y.id = Z.site_B_id)
                  )A)B"""
    
     # =================================================================================
    # Contains based on Chronological level
    # =================================================================================

    sel_6_cmd = """select product_name,
                        fp_status,
                        Orch_Connection,
                        Orch_LM_Type,
                        fcd_year,
                        fcd_month,
                        sum(site_count)
                   from (select 
                            case 
                                when product_name in ('Managed Single Internet Access','Single Internet Access') then 'IAS'
                                when product_name in ('Single managed GVPN','Single Unmanaged GVPN') then 'GVPN'
                            end as product_name,
                            fp_status,
                            Orch_Connection,
                            Orch_LM_Type,
                            year(feasibility_created_date) as fcd_year,
                            monthname(feasibility_created_date) as fcd_month,
                            count(distinct site_code) as site_count
                        from oms.vw_order_vs_pe_rcmd_site_cmp_20190627
                        where is_selected = 1
                        and product_name_fsbility is not null
                        and Orch_Connection is not null and Orch_Connection != 'NULL'
                        and Orch_LM_Type is not null and Orch_LM_Type != 'NULL'
                        and product_name in ('Managed Single Internet Access','Single Internet Access','Single managed GVPN','Single Unmanaged GVPN')
                        group by product_name, fp_status, Orch_Connection, Orch_LM_Type, year(feasibility_created_date), month(feasibility_created_date)
                        )X
                        group by product_name, fp_status, Orch_Connection, Orch_LM_Type, fcd_year, fcd_month

                    union

                    select 
                        'NPL' as product_name,
                        A.fp_status,
                        A.Orch_Connection,
                        A.Orch_LM_Type,
                        year(A.feasibility_created_date) as fcd_year,
                        monthname(A.feasibility_created_date) as fcd_month,
                        count(distinct C.link_code)as link_count
                    from oms.vw_order_vs_pe_rcmd_site_cmp_20190627 A
                    left outer join oms.order_ill_sites B
                    on A.site_code = B.site_code
                    left outer join oms.order_npl_link C
                    on (B.id = C.site_A_id 
                    or B.id = C.site_B_id)
                    where is_selected = 1
                    and product_name_fsbility is not null
                    and product_name in ('Private Line - NPL')
                    and A.feasibility_created_date != 'NULL'
                    group by product_name, fp_status, year(A.feasibility_created_date), month(A.feasibility_created_date)"""
    # =================================================================================
    # Initialization of class
    # =================================================================================

    def __init__(self):
        super(SqlTemplate, self).__init__()