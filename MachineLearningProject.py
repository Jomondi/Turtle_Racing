import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load csv file and display the columns
csv_file = pd.read_csv("chidata_for_assignment_5.csv")
print(csv_file.columns)
print()

# Convert the file into a dataframe and print the head/tail results
df = pd.DataFrame(csv_file)
print(df.head().to_markdown(tablefmt="grid"))
print()
print(df.tail().to_markdown(tablefmt="grid"))
print()


# Generate a seaborn countplot for gender
sns.countplot(x='Gender', data=df, palette='nipy_spectral')
plt.title('Gender Coverage')
plt.show()


# Generate a seaborn countplot for insurance
sns.countplot(x='Insurance', data=df, palette='nipy_spectral')
plt.title('Insurance Coverage')
plt.show()


# Create a contingency table
cont_tbl = pd.crosstab(df['Gender'],
                       df['Insurance'])
print(cont_tbl.to_markdown(tablefmt='grid'))


# Create a heatmap of the contigency table
sns.heatmap(cont_tbl, linecolor='white', linewidths=5)
plt.title('Contigency Map')
plt.show()