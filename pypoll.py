{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Voter ID</th>\n",
       "      <th>County</th>\n",
       "      <th>Candidate</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>12864552</td>\n",
       "      <td>Marsh</td>\n",
       "      <td>Khan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>17444633</td>\n",
       "      <td>Marsh</td>\n",
       "      <td>Correy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>19330107</td>\n",
       "      <td>Marsh</td>\n",
       "      <td>Khan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>19865775</td>\n",
       "      <td>Queen</td>\n",
       "      <td>Khan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>11927875</td>\n",
       "      <td>Marsh</td>\n",
       "      <td>Khan</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Voter ID County Candidate\n",
       "0  12864552  Marsh      Khan\n",
       "1  17444633  Marsh    Correy\n",
       "2  19330107  Marsh      Khan\n",
       "3  19865775  Queen      Khan\n",
       "4  11927875  Marsh      Khan"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "poll_df = pd.read_csv(\"Resources/PyPoll_Resources_election_data.csv\")\n",
    "poll_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "\n",
      "Total Votes 3521001 \n",
      "\n",
      "Khan: 63.0% (2218231)\n",
      "Correy: 20.0% (704200)\n",
      "Li: 14.0% (492940)\n",
      "O'Tooley: 3.0% (105630)\n",
      "\n",
      "Winner: Khan\n"
     ]
    }
   ],
   "source": [
    "i=0\n",
    "candidates = poll_df.Candidate.unique()\n",
    "votes_cast=int(poll_df.shape[0])\n",
    "candidate_count = poll_df.Candidate.value_counts()\n",
    "per_votes=[]\n",
    "for val in candidate_count:\n",
    "    per_votes.append(val/votes_cast)\n",
    "print(\"Election Results\\n\")\n",
    "print(\"Total Votes\",votes_cast,\"\\n\")\n",
    "for name in candidates:\n",
    "    print(f\"{name}: {round(per_votes[i]*100,1)}% ({candidate_count[i]})\")\n",
    "    i+=1\n",
    "print(\"\\nWinner:\",candidates[0])"
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
