#include <linux/module.h>
#include <linux/init.h>
#include <linux/proc_fs.h>
#include <linux/sched.h>
#include <linux/uaccess.h>
#include <linux/fs.h>
#include <linux/sysinfo.h>
#include <linux/seq_file.h>
#include <linux/slab.h>
#include <linux/mm.h>
#include <linux/swap.h>
#include <linux/rbtree.h>
#include <linux/hugetlb.h>
#include <linux/mman.h>
#include <linux/mmzone.h>
#include <linux/swap.h>
#include <linux/vmstat.h>
#include <linux/atomic.h>
#include <asm/page.h>
#include <asm/pgtable.h>

struct sysinfo i;
int lru;

static int show_cpu_percent(struct seq_file *m, void *v){
    #define K(x) ((x) << (PAGE_SHIFT - 10))
    si_meminfo(&i);
    seq_printf(m,"LIBRE: %8lu TOTAL: %8lu", K(i.freeram), K(i.totalram));   
    return 0;   
}

static ssize_t write_file_proc(struct file* file, const char __user *buffer, size_t count, loff_t *f_pos){
    return 0;
}

static int open_file_proc(struct inode *inode, struct file *file){
    return single_open(file, show_cpu_percent ,NULL);
}

static struct file_operations my_fops = {
    .owner = THIS_MODULE,
    .open = open_file_proc,
    .release = single_release,
    .read = seq_read,
    .llseek = seq_lseek,
    .write = write_file_proc
};

static int __init ram_read_percent_init(void){
    struct proc_dir_entry *entry;
    entry = proc_create("ram", 0777, NULL, &my_fops);
    if(!entry){
        return -1;
    } else {
        printk(KERN_INFO "Inicio RAM - Para llamar: cat /proc/ram\n");
    }
    return 0;
}

static void __exit ram_read_percent_exit(void){
    remove_proc_entry("ram", NULL);
    printk(KERN_INFO "Fin RAM\n");
}

module_init(ram_read_percent_init);
module_exit(ram_read_percent_exit);

MODULE_LICENSE("GPL");