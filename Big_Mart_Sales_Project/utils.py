import pandas as pd
import matplotlib.pyplot as plt
import io, base64
import matplotlib
matplotlib.use('Agg')  # <<< ADD THIS LINE

import pandas as pd
import matplotlib.pyplot as plt
import io, base64

def preview_data(file):
    df = pd.read_csv(file)
    return df.head().to_html(classes='table table-bordered table-striped', index=False)

def plot_sales_chart(file):
    df = pd.read_csv(file)
    plt.figure(figsize=(5,3))
    df['Item_Type'].value_counts().head(5).plot(kind='bar')
    plt.title('Top 5 Item Types')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode('utf-8')

