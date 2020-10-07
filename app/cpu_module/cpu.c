#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/cpufreq.h>

extern unsigned int arch_freq_get_on_cpu(int cpu);

__weak unsigned int arch_freq_get_on_cpu(int cpu)
{
  return 0;
}

int __init freqmod_init(void) {
  unsigned int f[2];
  
  printk(KERN_INFO "freqmod test init.\n");
  
  f[0] = arch_freq_get_on_cpu(0);
  f[1] = cpufreq_get(0);
    
  printk(KERN_ALERT ">> CPU Freq in KHz: %d\n", cpufreq_get(0) * 100000);
  printk(KERN_ALERT ">> CPU Freq in KHz: %d\n", cpufreq_get(1) * 1000);
  printk(KERN_ALERT ">> CPU Freq in KHz: %d\n", cpufreq_get(2));
  printk(KERN_INFO "arch freq=%u, cpufreq driver freq=%u\n",f[0],f[1]); 
  
  return 0;
}


void __exit freqmod_exit(void) {

  printk(KERN_INFO "freqmod test done.\n");
}

module_init(freqmod_init);
module_exit(freqmod_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Test <test@example.com>");
MODULE_DESCRIPTION("freqmod test");