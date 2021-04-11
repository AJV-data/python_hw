{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Anaysis \n",
      "\n",
      "Total Months: 86\n",
      "Total: $38382578\n",
      "Average Change $2315.1176470588234\n",
      "Greatest Increase in Profits: $1170593\n",
      "Greatest Decrease in Profits: $-1196225\n"
     ]
    }
   ],
   "source": [
    "month_count = 0\n",
    "sum_total = 0\n",
    "avg_change=0\n",
    "greatest_inc = 0\n",
    "greatest_dec = 0\n",
    "\n",
    "budget = \"Resources/budget-data.csv\"\n",
    "budget_df = pd.read_csv(budget)\n",
    "\n",
    "month_count = budget_df.Date.count()\n",
    "sum_total=budget_df[\"Profit/Losses\"].sum()\n",
    "greatest_inc=budget_df[\"Profit/Losses\"].max()\n",
    "greatest_dec=budget_df[\"Profit/Losses\"].min()\n",
    "\n",
    "p_l = list(budget_df[\"Profit/Losses\"])\n",
    "i=0\n",
    "temp = 0\n",
    "\n",
    "while i < len(p_l)-1:\n",
    "    avg_change+=(p_l[i]-p_l[i+1])\n",
    "    i+=1\n",
    "avg_change = avg_change/i\n",
    "\n",
    "print(\"Financial Anaysis \\n\")\n",
    "print(f\"Total Months: {month_count}\")\n",
    "print(f\"Total: ${sum_total}\")\n",
    "print(f\"Average Change ${avg_change}\")\n",
    "print(f\"Greatest Increase in Profits: ${greatest_inc}\")\n",
    "print(f\"Greatest Decrease in Profits: ${greatest_dec}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
