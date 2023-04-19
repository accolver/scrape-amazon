from scrape_amazon import get_reviews

reviews = get_reviews('com', 'B085BCWJV6') #returns dataframe
#SrNo.,Reviewer,ReviewerURL,VerifiedPurchase,HelpfulCount,Rating,Title,Description,Date

# https://www.amazon.com/HP-15-Computer-Touchscreen-Dual-Core/dp/B0863N5FM8/

print(reviews)
print(reviews.shape, reviews.describe())


# Product
# https://www.amazon.com/dp/[ASIN]

# Questions
# https://www.amazon.com/ask/questions/asin/[ASIN]/1?isAnswered=true
