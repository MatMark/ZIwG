const store = {
  namespaced: true,

  state: {
    cart_amount: 0,
    order_info: {
      shipment: undefined,
      payment: undefined,
      customer_data: undefined,
      updated: undefined
    },
    products: []
  },

  isTheSame(state, newProduct) {
    const personalization = JSON.stringify(newProduct.personalization);
    const index = state.products.findIndex(
      product =>
        product.product_id === newProduct.product_id &&
        JSON.stringify(product.personalization) === personalization
    );
    if (index !== -1) return index;
    else return false;
  },

  mutations: {
    ADD_PRODUCT(state, product) {
      state.cart_amount =
        (state.cart_amount * 100 + product.amount * (product.price * 100)) /
        100;
      const index = store.isTheSame(state, product);
      if (index === false) {
        product.sumPrice = (product.price * 100 * product.amount) / 100;
        state.products.push(product);
      } else {
        state.products[index].sumPrice +=
          (product.price * 100 * product.amount) / 100;
        state.products[index].amount += product.amount;
      }
    },
    EDIT_PRODUCT(state, edited) {
      // weird construction because array must be replaced not modified for computed properties
      const index = state.products.findIndex(
        product => product.order_id === edited.order_id
      );
      const temp = [...state.products];

      state.cart_amount = 0;
      for (const val of state.products) {
        state.cart_amount =
          (state.cart_amount * 100 + val.amount * val.price * 100) / 100;
      }

      edited.sumPrice = (edited.price * 100 * edited.amount) / 100;
      temp[index] = edited;
      state.products = temp;
    },
    REMOVE_PRODUCT(state, id) {
      const index = state.products.findIndex(
        product => product.order_id === id
      );
      state.cart_amount =
        (state.cart_amount * 100 -
          state.products[index].amount * state.products[index].price * 100) /
        100;
      state.products = state.products.filter(
        product => product.order_id !== id
      );
    },
    CLEAR_CART(state) {
      state.cart_amount = 0;
      state.products = [];
      state.order_info = {
        shipment: undefined,
        payment: undefined,
        customer_data: undefined,
        updated: undefined
      };
    },
    CLEAR_ORDER_INFO(state) {
      state.order_info = {
        shipment: undefined,
        payment: undefined,
        customer_data: undefined,
        updated: undefined
      };
    },
    CHANGE_SHIPMENT(state, shipment) {
      state.order_info.shipment = shipment;
      state.order_info.updated = Date.now();
    },
    CHANGE_PAYMENT(state, payment) {
      state.order_info.payment = payment;
      state.order_info.updated = Date.now();
    },
    CHANGE_CUSTOMER_DATA(state, customerData) {
      state.order_info.customer_data = customerData;
      state.order_info.updated = Date.now();
    }
  },

  actions: {
    addProduct(context, product) {
      context.commit("ADD_PRODUCT", product);
    },
    editProduct(context, edited) {
      context.commit("EDIT_PRODUCT", edited);
    },
    removeProduct(context, id) {
      context.commit("REMOVE_PRODUCT", id);
    },
    clearCart(context) {
      context.commit("CLEAR_CART");
    },
    clearOrderInfo(context) {
      context.commit("CLEAR_ORDER_INFO");
    },
    changeShipment(context, shipment) {
      context.commit("CHANGE_SHIPMENT", shipment);
    },
    changePayment(context, payment) {
      context.commit("CHANGE_PAYMENT", payment);
    },
    changeCustomerData(context, customerData) {
      context.commit("CHANGE_CUSTOMER_DATA", customerData);
    }
  },

  getters: {
    getProductsInCart(state) {
      return state.products;
    },
    getProductsIdsInCart(state) {
      const list = [];
      state.products.forEach(product => {
        list.push(parseInt(product.product_id));
      });
      return list;
    },
    getCartLength(state) {
      const sum = state.products
        .map(item => item.amount)
        .reduce((prev, curr) => prev + curr, 0);
      return sum;
    },
    getCartAmount(state) {
      if (state.cart_amount < 0) {
        state.cart_amount = 0;
      }
      return state.cart_amount;
    },
    getProductByOrderId: state => id => {
      return state.products.find(product => product.order_id === id);
    },
    getAmountByOrderId: state => id => {
      const product = state.products.find(product => product.order_id === id);
      return product.amount;
    },
    getShipment(state) {
      return state.order_info.shipment;
    },
    getPayment(state) {
      return state.order_info.payment;
    },
    getCustomerData(state) {
      return state.order_info.customer_data;
    },
    getOrderInfo(state) {
      return state.order_info;
    }
  }
};

export default store;
