**EV Smart Charging Platform**
An AI-powered Electric Vehicle smart charging and grid optimization dashboard built with Streamlit and Reinforcement Learning.

**Overview**
EV Smart Charging Platform is a web-based dashboard that uses a trained PPO (Proximal Policy Optimization) reinforcement learning agent to intelligently manage EV charging schedules, balance grid load, optimize solar energy usage, and reduce charging costs for users.
The platform supports two roles — User and Admin — each with their own tailored dashboard view.

**Features**
**User Dashboard**

Vehicle Status — Real-time battery level and estimated range display
Grid & Solar Metrics — Live grid status, solar discount availability, and ML-optimized cost estimate
AI Recommendation — Smart charging time suggestions to avoid peak load
Book a Slot — Schedule charging by date, time, and mode (Standard Grid / Solar Optimized / AI Recommended)
Emergency Charging — Instantly allocates highest-priority fast charging slot
AI Insights — 24-hour grid load chart with ML-driven peak predictions

**Admin Dashboard**

Grid Stability Index — Real-time stability score with visual indicator
Live Metrics — Active EVs currently charging, peak load forecast, solar efficiency
Grid Analytics — 24-hour grid load visualization
ML Priority Ranking — AI-ranked EV charging queue based on State of Charge (SoC), distance, and profession priority
Transformer Monitoring — Real-time voltage and current charts
Station Occupancy — Bar chart of charging station utilization across all stations
Smart Alerts — Automated alerts for high transformer load and demand balancing events


**AI / ML Components**
ComponentDetailsRL AgentPPO model (ev_agent) trained with Stable Baselines3Priority ScoringWeighted formula using SoC, travel distance, and profession urgencyLoad ForecastingPeak demand prediction to shift users to off-peak slotsCost OptimizationML-based charging cost minimization

**Tech Stack**
LayerTechnologyFrontend / UIStreamlitML / RLStable Baselines3 (PPO), NumPyData HandlingPandas, NumPyStylingCustom CSS (dark theme, glassmorphism cards)
