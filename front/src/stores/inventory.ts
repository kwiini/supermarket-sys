import { defineStore } from 'pinia';
import axios from 'axios';
import { ElMessage, ElMessageBox } from 'element-plus';

export interface Inventory {
  product_id: string;
  batch_number: string;
  production_date: string;
  expiry_date: string;
  quantity: number;
  location: string;
  inventory_id: string;
}

export const useInventoryStore = defineStore('inventory', {
    state: () => ({
        inventory: [] as Inventory[],
    }),
    actions: {
        async fetchInventory() {
            const response = await axios.get('http://127.0.0.1:8000/inventory');
            this.inventory = response.data;
        },
        async deleteInventory(id: string) {
            try {
                await ElMessageBox.confirm('确定要删除该库存记录吗？', '提示', {
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                    type: 'warning',
                });
                await axios.delete(`http://127.0.0.1:8000/inventory/${id}`);
                ElMessage.success('删除成功');
                await this.fetchInventory();
            } catch (error: any) {
                if (error === 'cancel' || error === 'close') {
                    ElMessage.info('已取消删除');
                } else {
                    console.error('删除失败:', error);
                    ElMessage.error('删除失败，请稍后重试');
                }
            }
        },
        async addInventory(data: any) {
            await axios.post('http://127.0.0.1:8000/inventory', data);
        }
    }
})