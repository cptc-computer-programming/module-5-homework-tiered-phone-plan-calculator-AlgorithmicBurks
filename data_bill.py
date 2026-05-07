# constant values are set here:
TIER_1_DATA_LIMIT_GB = 10
TIER_2_DATA_LIMIT_GB = 20
PREMIUM_USER_OVERAGE_RATE_TIER_2 = 1
REGULAR_USER_OVERAGE_RATE_TIER_2 = 2
PREMIUM_USER_OVERAGE_RATE_TIER_3 = 2
REGULAR_USER_OVERAGE_RATE_TIER_3 = 3
BASE_PLAN_COST = 50

# Your code goes here:

# Give a base plan cost amount
total = BASE_PLAN_COST

# Determine what plan the user has and data limit
# Ask for inputs
data_used = float(input("Enter GB used: "))
is_premium = input("Premium Plan user (yes/no)? ")







# Phone plan and determine is they are over
# we changed the rate_tier2/3 names because we needed to give a to simplfy the rates
if is_premium:
    rate_tier2 = PREMIUM_USER_OVERAGE_RATE_TIER_2
    rate_tier3 = PREMIUM_USER_OVERAGE_RATE_TIER_3
else:
    rate_tier2 = REGULAR_USER_OVERAGE_RATE_TIER_2
    rate_tier3 = REGULAR_USER_OVERAGE_RATE_TIER_3




# Output if the user is within the limit or over the limit
# we had to give the overage_tier a name so that we can determine what the overage is
if data_used <= TIER_1_DATA_LIMIT_GB:
    total = BASE_PLAN_COST
elif data_used <= TIER_2_DATA_LIMIT_GB:
    overage_tier2 = data_used - TIER_1_DATA_LIMIT_GB
    total = BASE_PLAN_COST + overage_tier2 * rate_tier2

else:
    overage_tier2 = TIER_2_DATA_LIMIT_GB - TIER_1_DATA_LIMIT_GB
    overage_tier3 = data_used - TIER_2_DATA_LIMIT_GB


# Print over or within the data limit
total = (BASE_PLAN_COST + overage_tier2 * rate_tier2 + overage_tier3 * rate_tier3)
print(f"Total bill: ${total:.2f}")