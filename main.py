from scrape_amazon import get_reviews, get_product

#SrNo.,Reviewer,ReviewerURL,VerifiedPurchase,HelpfulCount,Rating,Title,Description,Date
reviews = get_reviews('com', 'B085BCWJV6') #returns dataframe
print(reviews.columns)
print(reviews.shape, reviews.describe())
print("\n".join(reviews['Description'].tolist()))


# product = get_product('com', 'B085BCWJV6') #returns dataframe
# print(product)
