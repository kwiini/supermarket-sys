import { defineStore } from 'pinia';
import axios from 'axios';

interface Member {
  name: string;
  position: string;
  phone: string;
  email: string;
  hire_date: string;
  salary: number;
  manager_id: string;
  employee_id: string;
}

interface Product {
  id: number;
  name: string;
  price: number;
}

interface Sale {
  id: number;
  total_amount: number;
  date: string;
}

interface Supplier {
  id: number;
  name: string;
  contact: string;
}

interface Inventory {
  id: number;
  product_id: number;
  quantity: number;
}

interface Purchase {
  id: number;
  total_price: number;
  date: string;
}

export const useStore = defineStore('main', {
  state: () => ({
    members: [] as Member[],
    products: [] as Product[],
    sales: [] as Sale[],
    suppliers: [] as Supplier[],
    inventory: [] as Inventory[],
    purchases: [] as Purchase[],
  }),
  actions: {
    async fetchMembers() {
      const response = await axios.get('/employee');
      this.members = response.data;
      console.log(response.data)
    },
    async fetchProducts() {
      const response = await axios.get('/api/products');
      this.products = response.data;
    },
    async fetchSales() {
      const response = await axios.get('/api/sales');
      this.sales = response.data;
    },
    async fetchSuppliers() {
      const response = await axios.get('/api/suppliers');
      this.suppliers = response.data;
    },
    async fetchInventory() {
      const response = await axios.get('/api/inventory');
      this.inventory = response.data;
    },
    async fetchPurchases() {
      const response = await axios.get('/api/purchases');
      this.purchases = response.data;
    },
  },
});
