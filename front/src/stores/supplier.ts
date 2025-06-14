import { defineStore } from 'pinia';
import axios from 'axios';
import { ElMessage, ElMessageBox } from 'element-plus';

export interface Supplier {
  name: string;
  contact_person: string;
  phone: string;
  email: string;
  address: string;
  supply_category: string;
  supplier_id: string;
}

export const useSupplierStore = defineStore('supplier', {
    state: () => ({
        suppliers: [] as Supplier[],
    }),
    actions: {
        async fetchSuppliers() {
            const response = await axios.get('http://127.0.0.1:8000/supplier');
            // console.log(response.data)
            this.suppliers = response.data;
        },
        async deleteSuppliers(id: string) {
            try {
                await ElMessageBox.confirm('确定要删除该供应商吗？', '提示', {
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                    type: 'warning',
                });
                await axios.delete(`http://127.0.0.1:8000/supplier/${id}`);
                ElMessage.success('删除成功');
                await this.fetchSuppliers();
            } catch (error: any) {
                if (error === 'cancel' || error === 'close') {
                    ElMessage.info('已取消删除');
                } else {
                    console.error('删除失败:', error);
                    ElMessage.error('删除失败，请稍后重试');
                }
            }
        },
        async addSuppliers(data: any) {
            await axios.post('http://127.0.0.1:8000/supplier', data);
        }
    }
})