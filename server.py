from flask import Flask, request, jsonify
from src.Market import Market
from src.Order import Order, OrderType, Side
from src.InstructionQueue import InstructionType
import threading

# Define app and create Market instance
app = Flask(__name__)
market = Market("SPY")


# POST endpoint to submit orders
@app.route("/submit_order", methods=["POST"])
def submit_order():
    data = request.json

    try:
        # Read Enum values
        side = Side[data["side"].upper()]
        order_type = OrderType[data["order_type"].upper()]

        # Create Order obeject with data from request
        order = Order(
            order_id=None,
            side=side,
            quantity=data["quantity"],
            order_type=order_type,
            price=data.get("price")
        )

        # Add order to instruction queue as NEW_ORDER
        instr = order.to_instruction(InstructionType.NEW_ORDER)
        market.instruction_queue.add_instruction(instr)

        # Success: return order ID
        return jsonify({"status": "order received", "order_id": order.id}), 200

    # Failure: return error message
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# GET endpoint to retrieve order book
@app.route("/order_book", methods=["GET"])
def get_order_book():
    return market.order_book.__str__(), 200


# GET endpoint to retrieve executed trades
@app.route("/executed_trades", methods=["GET"])
def get_trades():
    return market.executed_trades.__str__(), 200


# Background thread to process instructions
def instruction_processor():

    # ALWAYS listen for new instructions
    while True:
        if not market.instruction_queue.is_empty():
            # Process next instruction
            market.matching_engine.process_next_instruction()


if __name__ == "__main__":

    # Start the instruction processor in a separate thread
    threading.Thread(target=instruction_processor, daemon=True).start()
    # Run the Flask app
    app.run(port=5000, debug=False)