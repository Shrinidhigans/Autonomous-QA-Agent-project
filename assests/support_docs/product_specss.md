# E-Shop Checkout - Product Specifications

## Version 1.0

**Last Updated:** November 2024

---

## 1. Product Catalog

### Available Products

1. **Wireless Headphones**

   - Product ID: 1
   - Price: $99.99
   - Category: Audio Equipment
   - In Stock: Yes

2. **Smart Watch**

   - Product ID: 2
   - Price: $199.99
   - Category: Wearable Technology
   - In Stock: Yes

3. **Bluetooth Speaker**
   - Product ID: 3
   - Price: $79.99
   - Category: Audio Equipment
   - In Stock: Yes

---

## 2. Shopping Cart Functionality

### Add to Cart

- Users can add products to cart by clicking "Add to Cart" button
- Each product can be added multiple times
- Quantity can be adjusted using the quantity input field
- Minimum quantity: 1 item
- Maximum quantity: 99 items per product

### Remove from Cart

- Users can remove individual items using the "Remove" button
- Cart updates automatically when items are removed

### Cart Persistence

- Cart data is stored in browser session
- Cart clears when browser is closed

---

## 3. Discount Code System

### Valid Discount Codes

#### SAVE15

- **Discount:** 15% off entire order
- **Minimum Purchase:** None
- **Valid Until:** December 31, 2025
- **Application:** Applied to subtotal before shipping

#### SAVE20

- **Discount:** 20% off entire order
- **Minimum Purchase:** $150.00
- **Valid Until:** December 31, 2025
- **Application:** Applied to subtotal before shipping

### Discount Rules

- Only one discount code can be applied per order
- Discount codes are case-insensitive
- Invalid codes display error message: "Invalid discount code"
- Empty code submission displays: "Please enter a discount code"
- Discount is calculated on subtotal (before shipping costs)
- Discount does not apply to shipping fees

### Discount Calculation Formula

```
Discount Amount = Subtotal × (Discount Percentage / 100)
Final Subtotal = Subtotal - Discount Amount
Total = Final Subtotal + Shipping Cost
```

---

## 4. Shipping Options

### Standard Shipping

- **Cost:** FREE ($0.00)
- **Delivery Time:** 5-7 business days
- **Availability:** All locations
- **Default Option:** Yes

### Express Shipping

- **Cost:** $10.00 (flat rate)
- **Delivery Time:** 2-3 business days
- **Availability:** All locations
- **Tracking:** Included

### Shipping Rules

- Shipping cost is added after discount calculation
- Standard shipping is selected by default
- Shipping method can be changed before payment
- Shipping cost does not qualify for discount codes

---

## 5. Payment Methods

### Credit Card

- **Accepted Cards:** Visa, MasterCard, American Express, Discover
- **Processing Time:** Immediate
- **Security:** PCI DSS compliant
- **Default Method:** Yes

### PayPal

- **Processing Time:** Immediate
- **Requirements:** Valid PayPal account
- **Security:** PayPal's standard security
- **Redirect:** No (simulated for demo)

---

## 6. Order Calculation Logic

### Price Calculation Order

1. Calculate subtotal (sum of all items × quantities)
2. Apply discount code (if valid)
3. Add shipping cost
4. Display final total

### Example Calculation

```
Cart:
- Wireless Headphones ($99.99) × 2 = $199.98
- Bluetooth Speaker ($79.99) × 1 = $79.99

Subtotal: $279.97
Discount (SAVE15 - 15%): -$41.99
Shipping (Express): +$10.00
TOTAL: $247.98
```

---

## 7. Customer Information Requirements

### Required Fields

- **Full Name:** Text input, minimum 2 characters
- **Email Address:** Must be valid email format (contains @ and domain)
- **Delivery Address:** Text input, minimum 5 characters
- **Shipping Method:** Radio button selection (required)
- **Payment Method:** Radio button selection (required)

### Validation Rules

- All required fields must be filled before payment
- Email must match pattern: [text]@[domain].[extension]
- Empty fields display specific error messages
- Form cannot be submitted with validation errors

---

## 8. Payment Processing

### Successful Payment Conditions

- Cart contains at least one item
- All required customer information is valid
- Shipping method is selected
- Payment method is selected

### Success Behavior

- Display "Payment Successful!" message in green
- Hide checkout form
- Show confirmation with order summary

### Failure Conditions

- Empty cart: Display "Your cart is empty!" alert
- Invalid customer information: Display field-specific errors
- Missing required fields: Highlight errors in red

---

## 9. Business Rules Summary

1. **Minimum Order:** No minimum order value
2. **Maximum Order:** No maximum order value
3. **Tax:** Not applicable (prices include all taxes)
4. **Currency:** USD only
5. **Refund Policy:** Not specified in checkout flow
6. **Guest Checkout:** Allowed (no account required)

---

## 10. Technical Specifications

### Supported Browsers

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

### Performance Requirements

- Page load time: < 2 seconds
- Cart update time: < 200ms
- Form validation: Real-time

### Accessibility

- WCAG 2.1 Level AA compliant
- Keyboard navigation supported
- Screen reader friendly

---

## Change Log

**Version 1.0 (November 2024)**

- Initial release
- Three products available
- Two discount codes active
- Two shipping options
- Two payment methods
