# Dataset - Wavecon 5G Launch Analysis

This folder contains the data files used for analyzing Wavecon Telecom's 5G launch impact.

## 📊 Data Files

### Main Dashboard File
- **Wavecon_dashboard_analysis1.pbix** - Power BI dashboard containing all visualization and data models

### Data Dictionary

The Power BI dashboard contains the following key metrics and dimensions:

#### Key Metrics (KPIs)
- **Total Revenue**: ₹31.9 Billion
- **ARPU** (Average Revenue Per User): ₹200.7
- **TAU** (Total Active Users): 161.7 Million
- **TUsU** (Total Unsubscribed Users): 12.6 Million
- **Revenue Change %**: -0.50% (Before vs After 5G)
- **Before 5G Revenue**: ₹16.0 Billion
- **After 5G Revenue**: ₹15.9 Billion

#### Geographic Dimensions
- **Cities Analyzed**: 15+ markets across India
  - Major metros: Mumbai, Delhi, Bangalore, Chennai, Kolkata, Hyderabad
  - Tier-2 cities: Lucknow, Jaipur, Ghaziabad, Gurgaon, Raipur, Coimbatore, Chandigarh
  - Other markets: Pune, Ahmedabad

#### Time Dimensions
- **Before 5G Launch**: Pre-launch revenue period
- **After 5G Launch**: Post-launch revenue period

## 📈 Data Schema

### City-Level Performance Metrics

| Column | Description | Data Type | Example |
|--------|-------------|-----------|---------|
| City | City/Market name | Text | Mumbai, Delhi, Chennai |
| Total_Revenue | Total revenue for the city | Currency (₹B) | 4.899 |
| Before_5G_Revenue | Revenue before 5G launch | Currency (₹B) | 2.448 |
| After_5G_Revenue | Revenue after 5G launch | Currency (₹B) | 2.452 |
| Revenue_Change_% | Percentage change in revenue | Percentage | 0.31% |
| Market_Tier | City tier classification | Text | Tier-1, Tier-2 |

### Aggregated Metrics

| Metric | Value | Unit |
|--------|-------|------|
| Total Revenue | 31.9 | Billion ₹ |
| Revenue Before 5G | 16.0 | Billion ₹ |
| Revenue After 5G | 15.9 | Billion ₹ |
| Revenue Change | -0.50 | % |
| ARPU | 200.7 | ₹ |
| Total Active Users | 161.7 | Million |
| Unsubscribed Users | 12.6 | Million |
| Monthly Average Revenue | 4.0 | Billion ₹ |

## 🔍 Data Quality Notes

- **Completeness**: All 15 cities have complete before/after 5G data
- **Accuracy**: Revenue figures rounded to billions (₹B)
- **Consistency**: All metrics use consistent time periods for before/after comparison
- **Granularity**: City-level aggregation (no plan-level granularity available in current data)

## 📁 Data Sources

- **Primary Source**: Wavecon Telecom internal dashboard (Power BI)
- **Data Period**: 5G launch transition period
- **Update Frequency**: Static snapshot (analysis period)

## 🎯 Analysis Focus Areas

1. **Revenue Impact Analysis**
   - Overall revenue change post-5G launch
   - City-wise revenue performance
   - Tier-1 vs Tier-2 comparison

2. **Geographic Performance**
   - Declining markets identification
   - Growing markets identification
   - Regional patterns and trends

3. **Customer Behavior**
   - User churn analysis (12.6M unsubscribed)
   - ARPU trends
   - Active user base analysis

## 📊 How to Use This Data

### Power BI Dashboard
1. Open `Wavecon_dashboard_analysis1.pbix` in Power BI Desktop
2. Refresh data if needed (data is embedded)
3. Explore interactive visualizations
4. Filter by city, time period, or metrics

### Python Analysis
```python
# The dashboard data is used in:
# - dashboard_analysis.py
# - create_enhanced_presentation.py

# Key metrics extracted:
metrics = {
    'Total Revenue': '₹31.9bn',
    'ARPU': '₹200.7',
    'TAU': '161.7M',
    'TUsU': '12.6M',
    'Revenue Change': '-0.50%'
}
```

## 🚫 Data Limitations

- **No plan-level data**: Individual plan performance not available
- **Limited time granularity**: Only before/after comparison, no time series
- **No customer demographics**: Age, income, usage patterns not included
- **No competitor data**: Market share and competitor metrics not available

## 📝 Data Attribution

- **Project**: CodeBasics Virtual Internship - Wavecon Telecom Analysis
- **Client**: Wavecon Telecom (fictional case study)
- **Analyst**: Theada Wright
- **Analysis Period**: December 2025

## 🔐 Data Privacy

This is a fictional dataset created for educational purposes as part of the CodeBasics Virtual Internship program. No real customer or business data is included.

---

For questions about the data or analysis methodology, refer to `INSIGHTS_SUMMARY.md` in the parent directory.
