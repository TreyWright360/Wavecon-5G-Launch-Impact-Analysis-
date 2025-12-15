"""
Wavecon 5G Launch Dashboard Analysis
Extracting insights from the dashboard preview
"""

import pandas as pd
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

# Key Metrics from Dashboard
metrics = {
    'Total Revenue': '₹31.9bn',
    'ARPU': '₹200.7',
    'TAU': '161.7M',
    'TUsU': '12.6M',
    'MA (Monthly Average)': '₹4.0bn',
    'Before 5G Revenue': '₹16.0bn',
    'After 5G Revenue': '₹15.9bn',
    'Revenue Change': '-0.50%'
}

# City-wise data from dashboard
city_data = {
    'Mumbai': {'total_rev': 4.899, 'before_5g': 2.448, 'after_5g': 2.452, 'chg': '0.31%'},
    'Delhi': {'total_rev': 3.877, 'before_5g': 1.964, 'after_5g': 1.908, 'chg': '-2.83%'},
    'Kolkata': {'total_rev': 3.844, 'before_5g': 1.925, 'after_5g': 1.918, 'chg': '-0.37%'},
    'Bangalore': {'total_rev': 3.396, 'before_5g': 1.667, 'after_5g': 1.699, 'chg': '0.75%'},
    'Chennai': {'total_rev': 2.964, 'before_5g': 1.501, 'after_5g': 1.457, 'chg': '-2.99%'},
    'Pune': {'total_rev': 2.598, 'before_5g': 1.265, 'after_5g': 1.301, 'chg': '0.27%'},
    'Hyderabad': {'total_rev': 2.357, 'before_5g': 1.185, 'after_5g': 1.171, 'chg': '-1.29%'},
    'Ahmedabad': {'total_rev': 1.871, 'before_5g': 0.943, 'after_5g': 0.916, 'chg': '-2.53%'},
    'Jaipur': {'total_rev': 1.492, 'before_5g': 0.751, 'after_5g': 0.736, 'chg': '0.98%'},
    'Lucknow': {'total_rev': 1.308, 'before_5g': 0.648, 'after_5g': 0.660, 'chg': '1.82%'},
    'Ghaziabad': {'total_rev': 0.882, 'before_5g': 0.467, 'after_5g': 0.495, 'chg': '1.42%'},
    'Coimbatore': {'total_rev': 0.514, 'before_5g': 0.257, 'after_5g': 0.257, 'chg': '0.11%'},
    'Chandigarh': {'total_rev': 0.312, 'before_5g': 0.207, 'after_5g': 0.305, 'chg': '-0.53%'},
    'Gurgaon': {'total_rev': 0.347, 'before_5g': 0.271, 'after_5g': 0.275, 'chg': '1.51%'},
    'Raipur': {'total_rev': 0.315, 'before_5g': 0.157, 'after_5g': 0.158, 'chg': '1.15%'},
}

print("="*80)
print("WAVECON 5G LAUNCH IMPACT ANALYSIS")
print("="*80)

print("\n1. KEY METRICS:")
print("-"*80)
for metric, value in metrics.items():
    print(f"{metric:<30}: {value}")

print("\n2. REVENUE IMPACT ANALYSIS:")
print("-"*80)
before_5g = 16.0
after_5g = 15.9
revenue_decline = before_5g - after_5g
decline_pct = -0.50

print(f"Revenue Before 5G: ₹{before_5g}bn")
print(f"Revenue After 5G:  ₹{after_5g}bn")
print(f"Revenue Decline:   ₹{revenue_decline}bn ({decline_pct}%)")
print(f"\n⚠️ INSIGHT: Revenue declined by ₹0.1bn (-0.50%) after 5G launch")

print("\n3. CITY-WISE PERFORMANCE:")
print("-"*80)

# Sort cities by change percentage
cities_sorted = sorted(city_data.items(), key=lambda x: float(x[1]['chg'].strip('%')))

print("\nWORST PERFORMING CITIES (Highest Revenue Decline):")
for i, (city, data) in enumerate(cities_sorted[:5], 1):
    print(f"{i}. {city:<15}: {data['chg']:>7} | Before: ₹{data['before_5g']}bn | After: ₹{data['after_5g']}bn")

print("\nBEST PERFORMING CITIES (Highest Revenue Growth):")
for i, (city, data) in enumerate(reversed(cities_sorted[-5:]), 1):
    print(f"{i}. {city:<15}: {data['chg']:>7} | Before: ₹{data['before_5g']}bn | After: ₹{data['after_5g']}bn")

print("\n4. KEY INSIGHTS:")
print("-"*80)
print("✓ Overall revenue declined by 0.50% post-5G launch")
print("✓ Chennai and Delhi showed largest revenue declines (-2.99% and -2.83%)")
print("✓ Lucknow and Ghaziabad showed positive growth (1.82% and 1.42%)")
print("✓ Mumbai, despite being largest market, showed minimal growth (0.31%)")
print("✓ ARPU: ₹200.7 - Average revenue per user")
print("✓ TAU: 161.7M - Total active users")

print("\n5. RECOMMENDATIONS:")
print("-"*80)
print("1. Investigate reason for revenue decline in Chennai and Delhi")
print("2. Study success factors in Lucknow and Ghaziabad for replication")
print("3. Monitor customer churn and plan performance metrics")
print("4. Consider plan adjustments or promotional offers in declining markets")
print("5. Analyze plan-wise performance to identify which plans are underperforming")

print("\n" + "="*80)
print("Analysis complete. Creating PowerPoint presentation...")
print("="*80)
