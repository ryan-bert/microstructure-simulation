import requests

BASE_URL = "http://127.0.0.1:5000"

def prompt_order():
    print("\n--- Submit New Order ---")

    # Get side
    while True:
        side = input("Side (buy/sell): ").strip().upper()
        if side in ["BUY", "SELL"]:
            break
        print("Invalid input. Please enter 'buy' or 'sell'.")

    # Get order type
    while True:
        order_type = input("Order Type (limit/market): ").strip().upper()
        if order_type in ["LIMIT", "MARKET"]:
            break
        print("Invalid input. Please enter 'limit' or 'market'.")

    # Get quantity
    while True:
        try:
            quantity = int(input("Quantity: ").strip())
            if quantity > 0:
                break
            print("Quantity must be a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")

    # Get price if it's a LIMIT order
    price = None
    if order_type == "LIMIT":
        while True:
            try:
                price = float(input("Limit Price: ").strip())
                break
            except ValueError:
                print("Please enter a valid number for price.")

    # Assemble payload
    payload = {
        "side": side,
        "order_type": order_type,
        "quantity": quantity
    }
    if price is not None:
        payload["price"] = price

    return payload

def submit_order(payload):
    try:
        resp = requests.post(f"{BASE_URL}/submit_order", json=payload)
        data = resp.json()
        if resp.status_code == 200:
            print(f"✅ Order submitted! Assigned Order ID: {data['order_id']}")
        else:
            print(f"❌ Server error: {data['error']}")
    except Exception as e:
        print(f"❌ Network or JSON error: {str(e)}")

def main():
    print("📡 Connected to Exchange @", BASE_URL)
    while True:
        payload = prompt_order()
        submit_order(payload)
        cont = input("\nSubmit another order? (y/n): ").strip().lower()
        if cont != 'y':
            break

if __name__ == "__main__":
    main()