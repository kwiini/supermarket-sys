import { defineStore } from 'pinia';
import axios from 'axios';
import { ElMessage, ElMessageBox } from 'element-plus';

export interface Purchase {
  supplier_id: string;
  product_id: string;
  purchase_date: string;
  quantity: number;
  unit_price: number;
  total_price: number;
  employee_id: string;
  purchase_id: string;
}

export const usePurchaseStore = defineStore('purchase', {
    state: () => ({
        purchases: [] as Purchase[],
    }),
    actions: {
        async fetchPurchases() {
            const response = await axios.get('http://127.0.0.1:8000/purchase');
            this.purchases = response.data;
        },
        async deletePurchases(id: string) {
            try {
                await ElMessageBox.confirm('确定要删除该采购记录吗？', '提示', {
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                    type: 'warning',
                });
                await axios.delete(`http://127.0.0.1:8000/purchase/${id}`);
                ElMessage.success('删除成功');
                await this.fetchPurchases();
            } catch (error: any) {
                if (error === 'cancel' || error === 'close') {
                    ElMessage.info('已取消删除');
                } else {
                    console.error('删除失败:', error);
                    ElMessage.error('删除失败，请稍后重试');
                }
            }
        },
        async addPurchases(data: any) {
            await axios.post('http://127.0.0.1:8000/purchase', data);
        }
    }
})