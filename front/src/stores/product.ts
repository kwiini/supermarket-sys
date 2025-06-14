import { defineStore } from 'pinia';
import axios from 'axios';
import { ElMessage, ElMessageBox } from 'element-plus';

export interface Product {
  name: string;
  category: string;
  purchase_price: number;
  selling_price: number;
  description: string;
  product_id: string;
}

export const useProductStore = defineStore('product', {
    state: () => ({
        products: [] as Product[],
    }),
    actions: {
        async fetchProducts() {
            const response = await axios.get('http://127.0.0.1:8000/product');
            this.products = response.data;
        },
        async deleteProducts(id: string) {
            try {
                await ElMessageBox.confirm('确定要删除该商品吗？', '提示', {
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                    type: 'warning',
                });
                await axios.delete(`http://127.0.0.1:8000/product/${id}`);
                ElMessage.success('删除成功');
                await this.fetchProducts();
            } catch (error: any) {
                if (error === 'cancel' || error === 'close') {
                    ElMessage.info('已取消删除');
                } else {
                    console.error('删除失败:', error);
                    ElMessage.error('删除失败，请稍后重试');
                }
            }
        },
        async addProducts(data: any) {
            await axios.post('http://127.0.0.1:8000/product', data);
        }
    }
})