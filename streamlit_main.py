# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe
st.markdown('Streamlit is **_really_ cool**.')
st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")
x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart
