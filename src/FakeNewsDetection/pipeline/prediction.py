from FakeNewsDetection.utils import stemming
import os
import joblib
from FakeNewsDetection import logger
import pandas as pd


class Prediction:
    def __init__(self, data: str):
        self.data = data

    def predict(self):
        # load model
        model_path = os.path.join('models', 'model.pkl')
        vectorizer_path = os.path.join('models', 'vectorizer.pkl')

        model = joblib.load(model_path)
        vectorizer = joblib.load(vectorizer_path)
        logger.info('Model and vectorizer loaded successfully')

        # convert  self.data to dataframe
        df = pd.DataFrame(self.data, columns=['text'])
        
        # keep only alphabets and numbers
        df['text'] = df['text'].str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)
        df['text'] = df['text'].str.lower()

            # perform stemming
        df['text'] = df['text'].apply(stemming)  
        logger.info("Stemming done")

        # vectorize data
        X = vectorizer.transform(df['text']).toarray()
        logger.info('Data vectorized successfully')

        # make prediction
        y_pred = model.predict(X)

        # return output
        print(y_pred)
        return y_pred



# test the prediction class

if __name__ == '__main__':
    data = ['WASHINGTON (Reuters) - Democratic Senator Elizabeth Warren is taking aim at budget chief Mick Mulvaney’s plan to fill the ranks of the U.S. consumer financial watchdog with political allies, according to letters seen by Reuters, the latest salvo in a broader battle over who should run the bureau. President Donald Trump last month appointed Mulvaney as acting director of the Consumer Financial Protection Bureau (CFPB), though the decision is being legally challenged by the agency’s deputy director, Leandra English, who says she is the rightful interim head. Mulvaney told reporters earlier this month he planned to bring in several political appointees to help overhaul the agency, but Warren warned in a pair of letters sent Monday to Mulvaney and the Office of Personnel Management (OPM), which oversees federal hiring, that doing so was inappropriate and potentially illegal. The CFPB is meant to be an independent agency staffed primarily by non-political employees. Hiring political appointees could violate civil service laws designed to protect such employees from undue political pressure and discrimination, Warren said. “Your naked effort to politicize the consumer agency runs counter to the agency’s mission to be an independent voice for consumers with the power to stand up to Wall Street banks,” Warren, who helped create the CFPB, wrote to Mulvaney. In a separate letter, Warren asked the OPM to review Mulvaney’s “unprecedented and unjustified” plans. In a third letter sent to Mulvaney and English, Warren asked for information about a review of ongoing enforcement actions at the CFPB. Reuters reported earlier this month that a potential multimillion-dollar settlement with Wells Fargo is among the enforcement actions under review amid the change in CFPB leadership. Spokespeople for Mulvaney and the OPM did not immediately respond to requests for comment. Mulvaney, who also serves directly under Trump as the head of his Office of Management and Budget (OMB), said in the long term he would like to see professional staff alongisde political appointees, mirroring an arrangement in place at the OMB.  “We will be staffing up with more permanent political people so the professional staff here have a better feel for where the administration wants to take the bureau,” Mulvaney said.  But Warren said such an arrangement, though understandable for bureaus like the OMB which sit directly beneath the White House, was not suitable for independent financial regulators. The leadership of the CFPB has been in question since the agency’s first director, Richard Cordray, resigned in November. ']
    prediction = Prediction(data)
    prediction.predict()