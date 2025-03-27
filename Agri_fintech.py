import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.set_page_config(
        page_title="AgriFinTech Credit Scorer 🌾",
        page_icon="🌾",
        layout="wide"
    )

    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(
            rgba(18, 18, 18, 0.95), 
            rgba(18, 18, 18, 0.95)
        ), url('https://images.unsplash.com/photo-1524000795694-8441141463e4?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80');
        background-size: cover;
        background-position: center;
        color: #ffffff;
        padding-top: 0 !important;
    }
    .main .block-container {
        background-color: transparent !important;
        padding-top: 0 !important;
    }
    .stApp > div {
        background-color: transparent !important;
        padding-top: 0 !important;
    }
    .stApp > div > div {
        background-color: transparent !important;
        padding-top: 0 !important;
    }
    .stApp > div > div > div {
        background-color: transparent !important;
        padding-top: 0 !important;
    }
    .stApp > div > div > div > div {
        background-color: transparent !important;
        padding-top: 0 !important;
    }
    .navbar {
        background: linear-gradient(90deg, #4CAF50, #45a049);
        padding: 1rem;
        margin-bottom: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        margin-top: 0 !important;
    }
    .navbar h1 {
        color: white;
        margin: 0;
        font-size: 2rem;
        text-align: center;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .stNumberInput input, .stSelectbox select {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #4CAF50 !important;
    }
    .stNumberInput label, .stSelectbox label {
        color: #ffffff !important;
    }
    .metric-card {
        background-color: rgba(45, 45, 45, 0.8);
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .metric-box {
        background-color: rgba(45, 45, 45, 0.9);
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        border-left: 5px solid #4CAF50;
        color: #ffffff;
    }
    .financial-box {
        border-left-color: #2196F3;
    }
    .agricultural-box {
        border-left-color: #FF9800;
    }
    .risk-box {
        border-left-color: #F44336;
    }
    .score-box {
        background: linear-gradient(135deg, #4CAF50, #45a049);
        color: white;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }
    .stMarkdown {
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="navbar">
        <h1>🌾 Agri FinTech</h1>
    </div>
    """, unsafe_allow_html=True)

    class EnhancedCreditScoringSystem:
        @staticmethod
        def calculate_comprehensive_metrics(inputs):
            try:
                total_revenue = float(inputs.get('Total Revenue', 0))
                total_expenses = float(inputs.get('Total Expenses', 0))
                loan_payment = float(inputs.get('Loan Payment Obligation', 0))
                crop_yield = float(inputs.get('Actual Yield', 0))
                expected_yield = float(inputs.get('Expected Yield', 0))
                input_costs = float(inputs.get('Input Costs', 0))
                farm_size = float(inputs.get('Farm Size', 0))

                if total_revenue <= 0 or total_expenses <= 0 or crop_yield <= 0 or expected_yield <= 0:
                    st.error("Please enter valid values for revenue, expenses, and yields.")
                    return {}

                net_profit = total_revenue - total_expenses
                profit_margin = (net_profit / total_revenue * 100)
                yield_efficiency = (crop_yield / expected_yield * 100)
                input_cost_ratio = input_costs / crop_yield
                debt_service_ratio = loan_payment / total_revenue if total_revenue > 0 else 0
                
                base_score = 50
                
                financial_score = 0
                
                if total_revenue > 2000000:
                    financial_score += 15
                elif total_revenue > 1000000:
                    financial_score += 12
                elif total_revenue > 500000:
                    financial_score += 9
                elif total_revenue > 100000:
                    financial_score += 6
                else:
                    financial_score += 3
                
                if profit_margin > 40:
                    financial_score += 15
                elif profit_margin > 25:
                    financial_score += 12
                elif profit_margin > 15:
                    financial_score += 9
                elif profit_margin > 5:
                    financial_score += 6
                else:
                    financial_score += 3
                
                if debt_service_ratio == 0:
                    financial_score += 10
                elif debt_service_ratio < 0.2:
                    financial_score += 8
                elif debt_service_ratio < 0.4:
                    financial_score += 6
                elif debt_service_ratio < 0.6:
                    financial_score += 3
                else:
                    financial_score += 1
                
                agricultural_score = 0
                
                if yield_efficiency > 95:
                    agricultural_score += 15
                elif yield_efficiency > 85:
                    agricultural_score += 12
                elif yield_efficiency > 75:
                    agricultural_score += 9
                elif yield_efficiency > 65:
                    agricultural_score += 6
                else:
                    agricultural_score += 3
                
                if input_cost_ratio < 0.2:
                    agricultural_score += 15
                elif input_cost_ratio < 0.3:
                    agricultural_score += 12
                elif input_cost_ratio < 0.4:
                    agricultural_score += 9
                elif input_cost_ratio < 0.5:
                    agricultural_score += 6
                else:
                    agricultural_score += 3
                
                scale_score = 0
                
                if farm_size > 100:
                    scale_score += 15
                elif farm_size > 50:
                    scale_score += 12
                elif farm_size > 25:
                    scale_score += 9
                elif farm_size > 10:
                    scale_score += 6
                else:
                    scale_score += 3
                
                if loan_payment == 0:
                    scale_score += 15
                elif debt_service_ratio < 0.2:
                    scale_score += 12
                elif debt_service_ratio < 0.4:
                    scale_score += 9
                elif debt_service_ratio < 0.6:
                    scale_score += 6
                else:
                    scale_score += 3
                
                credit_score = base_score + (
                    (financial_score * 0.4) +
                    (agricultural_score * 0.3) +
                    (scale_score * 0.3)
                )
                
                credit_score = max(0, min(credit_score, 100))

                return {
                    'Net Profit': net_profit,
                    'Profit Margin (%)': profit_margin,
                    'Yield Efficiency (%)': yield_efficiency,
                    'Input Cost Ratio': input_cost_ratio,
                    'Farm Size Impact': farm_size * 0.2,
                    'Financial Score': financial_score,
                    'Agricultural Score': agricultural_score,
                    'Scale Score': scale_score,
                    'Credit Score': credit_score
                }
            except Exception as e:
                st.error(f"Detailed Error in Metric Calculation: {e}")
                return {}

        @staticmethod
        def get_loan_recommendation(credit_score):
            recommendations = [
                {
                    'range': (80, 100),
                    'status': "Platinum: Maximum Loan Eligibility",
                    'color': "green",
                    'description': "Exceptional financial and agricultural performance. Lowest interest rates."
                },
                {
                    'range': (60, 80),
                    'status': "Gold: Strong Loan Approval",
                    'color': "blue",
                    'description': "Solid performance. Favorable loan terms."
                },
                {
                    'range': (40, 60),
                    'status': "Silver: Conditional Approval",
                    'color': "orange",
                    'description': "Moderate risk. May require additional guarantees."
                },
                {
                    'range': (0, 40),
                    'status': "Bronze: Limited Options",
                    'color': "red",
                    'description': "High risk. Requires comprehensive risk mitigation."
                }
            ]

            for rec in recommendations:
                if rec['range'][0] <= credit_score < rec['range'][1]:
                    return rec
            
            return recommendations[-1]

    st.title("🌾 زراعت کریڈٹ سکورنگ سسٹم")
    st.markdown("### Empowering Farmers through Financial Intelligence")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 🏡 Farm Specifics")
        farm_size = st.number_input(
            "Farm Size (acres)", 
            min_value=0.0,
            help="Total cultivated land area"
        )
        crop_type = st.selectbox(
            "Primary Crop", 
            ["Wheat", "Rice", "Corn", "Sugarcane", "Vegetables", "Fruits"],
            help="Type of crop cultivated"
        )
        irrigation_type = st.selectbox(
            "Irrigation Method", 
            ["Rain-fed", "Canal", "Tube well", "Drip Irrigation"],
            help="Water management technique"
        )

    with col2:
        st.markdown("#### 💰 Financial Metrics")
        total_revenue = st.number_input(
            "Annual Revenue (PKR)", 
            min_value=0.0,
            help="Total income from agricultural produce"
        )
        total_expenses = st.number_input(
            "Annual Expenses (PKR)", 
            min_value=0.0,
            help="Total farming-related expenditures"
        )
        loan_payment = st.number_input(
            "Current Loan Obligation (PKR)", 
            min_value=0.0,
            help="Existing loan repayment amount"
        )

    st.markdown("#### 🌱 Crop Yield Insights")
    col3, col4 = st.columns(2)

    with col3:
        expected_yield = st.number_input(
            "Expected Yield (kg)", 
            min_value=0.0,
            help="Projected crop production"
        )
    
    with col4:
        actual_yield = st.number_input(
            "Actual Yield (kg)", 
            min_value=0.0,
            help="Realized crop production"
        )

    input_costs = st.number_input(
        "Total Input Costs (PKR)", 
        min_value=0.0,
        help="Expenses on seeds, fertilizers, labor, etc."
    )

    if st.button("🔍 Calculate Credit Score", use_container_width=True):
        inputs = {
            'Total Revenue': total_revenue,
            'Total Expenses': total_expenses,
            'Loan Payment Obligation': loan_payment,
            'Expected Yield': expected_yield,
            'Actual Yield': actual_yield,
            'Input Costs': input_costs,
            'Farm Size': farm_size
        }

        results = EnhancedCreditScoringSystem.calculate_comprehensive_metrics(inputs)
        
        if results:
            st.markdown("## 📊 Credit Assessment Report")
            
            fig = plt.figure(figsize=(10, 6))
            
            metrics = ['Net Profit', 'Credit Score', 'Yield Efficiency']
            values = [
                results['Net Profit'] / 1000,
                results['Credit Score'],
                results['Yield Efficiency (%)']
            ]
            
            bars = plt.bar(metrics, values, color=['#4CAF50', '#2196F3', '#FF9800'])
            
            plt.title('Key Performance Metrics', pad=20)
            plt.ylabel('Value')
            
            for bar in bars:
                height = bar.get_height()
                if metrics[bars.index(bar)] == 'Net Profit':
                    plt.text(bar.get_x() + bar.get_width()/2., height,
                            f'PKR {int(height)}K',
                            ha='center', va='bottom')
                else:
                    plt.text(bar.get_x() + bar.get_width()/2., height,
                            f'{int(height)}',
                            ha='center', va='bottom')
            
            plt.tight_layout()
            
            st.pyplot(fig)
            
            st.markdown("""
            <div class="metric-box" style='background-color: rgba(45, 45, 45, 0.9);'>
                <h4 style='color: #4CAF50;'>📈 Performance Overview:</h4>
                <p style='color: #ffffff;'>Key metrics showing Net Profit (in thousands PKR), Credit Score, and Yield Efficiency percentage.</p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                <div class="metric-box financial-box">
                    <h3 style='color: #2196F3;'>Financial Health</h3>
                </div>
                """, unsafe_allow_html=True)
                st.markdown(f"""
                <div style='background-color: rgba(33, 150, 243, 0.1); padding: 15px; border-radius: 10px; margin: 10px 0;'>
                    <p style='color: #ffffff; margin: 5px 0;'>Net Profit: <span style='color: #2196F3; font-weight: bold;'>PKR {results['Net Profit']:,.2f}</span></p>
                    <p style='color: #ffffff; margin: 5px 0;'>Profit Margin: <span style='color: #2196F3; font-weight: bold;'>{results['Profit Margin (%)']:,.2f}%</span></p>
                    <p style='color: #ffffff; margin: 5px 0;'>Financial Score: <span style='color: #2196F3; font-weight: bold;'>{results['Financial Score']}/40</span></p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div class="metric-box agricultural-box">
                    <h3 style='color: #FF9800;'>Agricultural Performance</h3>
                </div>
                """, unsafe_allow_html=True)
                st.markdown(f"""
                <div style='background-color: rgba(255, 152, 0, 0.1); padding: 15px; border-radius: 10px; margin: 10px 0;'>
                    <p style='color: #ffffff; margin: 5px 0;'>Yield Efficiency: <span style='color: #FF9800; font-weight: bold;'>{results['Yield Efficiency (%)']:,.2f}%</span></p>
                    <p style='color: #ffffff; margin: 5px 0;'>Input Cost Ratio: <span style='color: #FF9800; font-weight: bold;'>{results['Input Cost Ratio']:,.2f}</span></p>
                    <p style='color: #ffffff; margin: 5px 0;'>Agricultural Score: <span style='color: #FF9800; font-weight: bold;'>{results['Agricultural Score']}/30</span></p>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown("""
                <div class="metric-box risk-box">
                    <h3 style='color: #F44336;'>Scale & Risk</h3>
                </div>
                """, unsafe_allow_html=True)
                st.markdown(f"""
                <div style='background-color: rgba(244, 67, 54, 0.1); padding: 15px; border-radius: 10px; margin: 10px 0;'>
                    <p style='color: #ffffff; margin: 5px 0;'>Farm Size Impact: <span style='color: #F44336; font-weight: bold;'>{results['Farm Size Impact']:.2f}</span></p>
                    <p style='color: #ffffff; margin: 5px 0;'>Scale Score: <span style='color: #F44336; font-weight: bold;'>{results['Scale Score']}/30</span></p>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class="score-box">
                <h2 style='margin-bottom: 10px;'>Overall Credit Score</h2>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style='background-color: #f0f0f0; border-radius: 10px; padding: 20px;'>
                <div style='background: linear-gradient(90deg, #4CAF50 {results['Credit Score']}%, #f0f0f0 {results['Credit Score']}%); 
                            height: 30px; 
                            border-radius: 15px; 
                            display: flex; 
                            align-items: center; 
                            justify-content: center; 
                            color: white; 
                            font-weight: bold;'>
                    {results['Credit Score']:.1f}/100
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            credit_score = results['Credit Score']
            recommendation = EnhancedCreditScoringSystem.get_loan_recommendation(credit_score)
            
            st.markdown(f"""
            <div class="metric-box" style='background-color: {recommendation['color']}20; border-left-color: {recommendation['color']};'>
                <h3 style='color: {recommendation['color']};'>{recommendation['status']}</h3>
                <p>{recommendation['description']}</p>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
    